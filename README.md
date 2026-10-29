# Stories website

Standalone, static English website for Stories (RedditTikTok Studio).
Operator: Ravil Faizrahmanov (Файзрахманов Равиль Равильевич), independent
individual developer, Republic of Kazakhstan. No company/legal entity is represented.

## Status: approved for publication; live deployment pending

On 29 October 2026 the owner confirmed the legal documents, operator name and
public contact reddittiktokstudio.support@gmail.com and explicitly authorized
creation of PUBLIC LincoreSvastom/stories-website, website-only push and GitHub Pages
publication. The documents are prepared with effective/updated date 29 October 2026.
A successful live deployment must still be independently verified before reporting
its URLs. Desktop source and user data are excluded.

## Repository separation

Public website-only repository: `https://github.com/LincoreSvastom/stories-website`.
Repository creation and Public visibility were verified on 29 October 2026. Live Pages deployment is pending verification.
Do not copy desktop source, its Git history, databases, tokens, config, screenshots
with private paths, videos, logs or binaries here. Do not repurpose existing repositories.
The desktop repository remains local; if later hosted it must stay private unless
the owner expressly authorizes otherwise. This repo has an independent Git history.

## Preview and checks

```text
python scripts/validate.py
python scripts/stage.py
python -m http.server 8768 --bind 127.0.0.1 --directory _site
```

No Node build, external font, analytics, JavaScript, account form or token exchange.
Relative links support a GitHub Pages project subpath.

## Required steps before public actions

1. Keep the confirmed PUBLIC support/privacy email consistent on all three pages.
2. Review the legal text with the operator. Confirm the offered distribution/support
   and data practices still match the code. Set actual effective/updated dates.
3. Remove the draft banner, draft wording and noindex metadata only after final review.
4. Run `python scripts/stage.py --publish`; it must pass.
5. Obtain explicit approval to CREATE the public repository, PUSH the website-only
   commit, and ENABLE/PUBLISH GitHub Pages. These are separate external actions;
   local preparation is not permission to perform them.
6. Create public `stories-website` with no desktop application content. Inspect staged
   files and secret scan before pushing this repository's main branch.
7. Settings → Pages → Build and deployment → Source: GitHub Actions.
   Use a deployment environment approval rule if desired.
8. Manually run the Pages workflow with confirmation `PUBLISH_STORIES` after approval.
   It does not publish on push and rejects unfinished documents.
9. Read the returned deployment URL. Independently verify HTTPS 200 for Home,
   Privacy Policy and Terms of Service, page titles, legal links and mobile layout.
   Only then enter VERIFIED URLs in TikTok Developers and report them as live.

GitHub account authentication is provided by the connected GitHub MCP. This session's
connector supports repository/file operations but exposes no repository-creation or
Pages administration tool; GitHub CLI is not installed. After approval, creation/
Pages setup may need an authenticated GitHub browser session or separately configured
CLI. Never export connector tokens or insert credentials into commands, source or URLs.

Expected project URL shape is documented by GitHub, but no suggested URL is a verified
live site. No CNAME or domain verification record is invented. A TikTok domain/URL
verification file, if requested, must be supplied by the owner and reviewed separately.

## Assets published by the workflow

Only index.html, privacy.html, terms.html, styles.css, favicon.svg and .nojekyll are
copied to `_site/`. README, scripts, Git metadata and integration notes are not deployed.
The public repository would still expose its committed source and history, so review
the entire commit, not only `_site/`, before approving publication.

## Platform references

- [GitHub Pages hosting](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [TikTok Desktop Login Kit](https://developers.tiktok.com/docs/en/login-kit-desktop)
- [TikTok scopes](https://developers.tiktok.com/docs/en/tiktok-api-scopes)
- [TikTok content sharing requirements](https://developers.tiktok.com/docs/en/content-sharing-guidelines)
- [TikTok app review](https://developers.tiktok.com/docs/en/app-review-guidelines)
- [YouTube developer policies](https://developers.google.com/youtube/terms/developer-policies)

The website does not imply a successful platform review. A static site alone does not
make the current desktop integration eligible for TikTok public Direct Post.
