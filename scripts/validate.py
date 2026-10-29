"""Static-site preflight. Publish mode rejects unfinished legal/contact fields."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
PUBLIC_FILES=('index.html','privacy.html','terms.html','styles.css','favicon.svg','.nojekyll')


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=set()
        self.links=[]
        self.headings=0
        self.lang=False
        self.title=False
    def handle_starttag(self,tag,attrs):
        data=dict(attrs)
        if 'id' in data:
            if data['id'] in self.ids:raise ValueError('Duplicate HTML id: '+data['id'])
            self.ids.add(data['id'])
        if tag=='h1':self.headings+=1
        if tag=='html':self.lang=data.get('lang')=='en'
        if tag=='title':self.title=True
        if tag=='img' and 'alt' not in data:raise ValueError('Image lacks alt attribute')
        for key in ('href','src'):
            if key in data:self.links.append(data[key])
        if tag in ('script','iframe','form'):raise ValueError('Unexpected active/third-party content')


def validate(publish=False):
    pages={}
    for name in PUBLIC_FILES:
        if not (ROOT/name).is_file():raise ValueError('Missing public asset: '+name)
    for name in ('index.html','privacy.html','terms.html'):
        text=(ROOT/name).read_text(encoding='utf-8')
        page=Page();page.feed(text)
        if page.headings!=1 or not page.lang or not page.title:raise ValueError('Invalid page landmarks: '+name)
        if publish and any(marker in text for marker in ('TODO:','Unpublished review draft','noindex,nofollow','not yet effective')):
            raise ValueError('Publication blocked: unfinished contact/date/review state in '+name)
        if publish:
            emails=re.findall(r'href="mailto:([^"?]+)"',text)
            if not emails or any(not re.fullmatch(r'[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+',email) for email in emails):
                raise ValueError('Publication blocked: a valid public contact email is required on '+name)
        if re.search(r'gh[pousr]_[A-Za-z0-9]{30,}|AIza[A-Za-z0-9_-]{30,}|-----BEGIN .*PRIVATE KEY-----',text):
            raise ValueError('Potential credential in '+name)
        pages[name]=page
    for name,page in pages.items():
        for link in page.links:
            parsed=urlsplit(link)
            if parsed.scheme:
                if parsed.scheme not in ('https','mailto'):raise ValueError('Unsafe external scheme: '+link)
                continue
            if parsed.netloc:raise ValueError('Protocol-relative URL is not allowed')
            relative=unquote(parsed.path) or name
            target=(ROOT/relative).resolve()
            if target.parent!=ROOT or relative not in PUBLIC_FILES or not target.is_file():
                raise ValueError('Invalid local asset: '+link)
            if parsed.fragment:
                if relative not in pages or unquote(parsed.fragment) not in pages[relative].ids:
                    raise ValueError('Broken fragment: '+name+' -> '+link)
    home=pages['index.html']
    if not {'privacy.html','terms.html'}.issubset(set(home.links)):
        raise ValueError('Legal links must be directly visible from home')
    print('PASS: 3 English pages; local links, fragments, assets and secret patterns checked.')
    if not publish:print('PREVIEW ONLY: confirm final documents, actual effective date and publication approval before release.')


if __name__=='__main__':
    try:validate('--publish' in sys.argv)
    except ValueError as exc:
        print(str(exc),file=sys.stderr)
        raise SystemExit(1)
