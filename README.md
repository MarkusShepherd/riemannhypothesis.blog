# Understanding the Riemann Hypothesis

Source of [riemannhypothesis.blog](https://riemannhypothesis.blog/), built with
[Hugo](https://gohugo.io/) and the
[Beautiful Hugo](https://github.com/halogenica/beautifulhugo) theme.

## Requirements

| Tool | Version | Pinned in |
| --- | --- | --- |
| Hugo (standard) | 0.170.1 | `.gitlab-ci.yml` (`default.image`) |
| Beautiful Hugo | v5.2.1 (`7f003819`) | `themes/beautifulhugo` submodule |

Install Git and [Hugo 0.170.1](https://github.com/gohugoio/hugo/releases/tag/v0.170.1).
Use the same Hugo version locally (`hugo version`). CI fails on build warnings
with `--panicOnWarning`.

## Building from a clean checkout

```sh
git clone --recurse-submodules https://gitlab.com/mshepherd/riemannhypothesis.blog.git
cd riemannhypothesis.blog
# Or, in an existing clone:
git submodule update --init --recursive

hugo version
hugo server                       # Preview on http://localhost:1313/
hugo --minify --panicOnWarning     # Production build into public/
```

Use `hugo server --buildDrafts` to preview draft content. Generated `public/`
output is ignored by Git.

Posts live in `content/posts/`; about and project pages have their own content
sections. Published posts set their historical URLs in front matter. Static
images, PDFs and scripts live in `static/`. The Python experiments under
`experiments/` are independent of the Hugo build.

## CI and deployment

GitLab CI uses `ghcr.io/gohugoio/hugo:v0.170.1` and initializes submodules
recursively. It runs branch pipelines without separate merge request or tag
pipelines:

- `test` builds every branch other than `$CI_DEFAULT_BRANCH`.
- `deploy` builds the default branch and publishes `public/` to GitLab Pages.

Both jobs run `hugo --minify --panicOnWarning`. Deployment artifacts are retained
for 48 hours; that retention setting does not expire the published Pages site.

## Site-specific configuration

- `hugo.yaml` holds branding, navigation, author/social links and tag-based
  related-post settings.
- Its file mounts publish five canonical PDFs at their historical
  `/wp-content/uploads/2014/...` download URLs. Preserve both the canonical
  paths and these legacy paths when changing the files or build setup.
- `Params.images` supplies the logo as the fallback Open Graph preview image.
- Existing math uses escaped delimiters and the theme's client-side KaTeX
  rendering. Standard Goldmark passthrough settings prevent math assets loading
  with this content; test delimiter handling before enabling them.
- Raw HTML is enabled for existing content. `layouts/robots.txt` supplies the
  site's robots file. RSS uses Hugo's embedded template with post summaries.

## Updating Hugo and the theme

This procedure follows the shared maintenance approach used by
[Analysis Paralysis](https://gitlab.com/recommend.games/blog). Keep common
versions and CI conventions aligned while preserving each site's content,
branding and asset requirements.

1. Read the [Hugo release notes](https://github.com/gohugoio/hugo/releases)
   and the theme's commits and migration guides since the pinned revision.
2. Build the current pin and the candidate from clean checkouts using their
   explicit official images (`ghcr.io/gohugoio/hugo:<version>`).
3. Compare generated paths, redirects, RSS, sitemap entries and normalized HTML.
   Check image/video targets and counts, including previews on listing pages.
   Verify the historical PDF paths against their canonical files.
4. Check formula-heavy articles, menus, author links and media on desktop and
   mobile. Run `hugo --logLevel info` to inspect deprecation notices and require
   a clean `hugo --minify --panicOnWarning` build.
5. Update the CI image, theme submodule and version table above together. Check
   the branch pipeline before merging and verify Pages after deployment. Record
   intentional differences and outstanding validation in the merge request.
