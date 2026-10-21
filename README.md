# Dickson Owuor · Research & Owuor Lab

A lightweight Jekyll site for [owuordickson.github.io](https://owuordickson.github.io), with About, Publications, Service, Teaching, and Owuor Lab pages. Content is based on the supplied CV. Core content and navigation work without JavaScript or external fonts.

## Run locally

Install Ruby 3.4 and Bundler using your preferred Ruby version manager. On macOS with Homebrew:

```sh
brew install ruby@3.4
export PATH="$(brew --prefix ruby@3.4)/bin:$PATH"
```

From the repository root:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --livereload
```

Open <http://localhost:4000>. Stop the server with Ctrl+C. Restart it after changing `_config.yml`. Dependencies and generated files are ignored; commit `Gemfile.lock` when updating dependencies.

## Edit content

| Content | File | How to update |
| --- | --- | --- |
| Biography, education, research interests | `index.md` | Edit the narrative and semantic HTML blocks. |
| Publications | `_data/publications.yml` | Add `title`, `authors`, integer `year`, `type`, and `venue`; optional `doi`, `url`, `pages`. |
| Reviews, committees, leadership, memberships | `_data/service.yml` | Update the relevant named list. |
| Courses and doctoral supervision | `_data/teaching.yml` | Update `courses` or students under the Completed/Ongoing groups. |
| Lab research and contact | `lab.md` | Edit the research narrative. |
| Navigation | `_data/navigation.yml` | Keep titles and URLs consistent with page permalinks. |
| Contact and canonical URL | `_config.yml` | Update site metadata and rebuild. |
| CV | `assets/documents/owuor.pdf` | Replace with the intended public PDF, keeping the filename. |
| Lab logo | `assets/images/owlab-green.png` | Replace the PNG; preserve aspect ratio and update dimensions in `lab.md` if needed. |
| Layout and visual design | `_layouts/`, `_includes/`, `assets/css/main.css` | Shared presentation across all pages. |

Publication types are `Journal article`, `International conference`, `National conference`, `Software`, and `Dataset`. The page groups records by year automatically. Store DOI identifiers without the `https://doi.org/` prefix; omit links when no verified source is available. YAML strings containing a colon must be quoted. The validator currently expects the initial CV's 26 entries and category totals; update that expectation deliberately when adding or recategorizing publications.

The initial content preserves the detailed CV's three completed and two ongoing doctoral supervisions, with tentative dates labelled accordingly. Review roles and appointments periodically. Review contact details in each replacement CV before publishing it.

## Validate

Python 3 is used only for validation, with no extra Python dependencies.

```sh
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter --trace
python3 scripts/validate_site.py _site
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter --baseurl /preview --destination _site-preview
python3 scripts/validate_site.py _site-preview /preview
git diff --check
```

Validation checks all five pages and the 404 page, navigation and active state, metadata, all local URLs and fragments, image alternatives, publication categories, DOI formatting, the CV download, and exclusion of development files. It does not contact external sites. Also review pages in a browser at mobile and desktop widths, including keyboard focus and long citations.

## GitHub Pages

The workflow in `.github/workflows/pages.yml` builds and validates pull requests with read-only repository permissions. Pushes to `main` build and deploy the validated `_site` artifact; only the deployment job receives Pages and OIDC write permissions. This PR does not merge itself or change repository settings.

Before the first deployment, select **Settings → Pages → Build and deployment → Source → GitHub Actions** in the repository. Ensure the `github-pages` environment permits deployment from `main`. After merging, inspect the Actions run and visit <https://owuordickson.github.io>.

For a project site, set `baseurl` to the repository subpath (for example `/research`) and adjust the workflow's production validation invocation to pass that base path as its second argument. Keep `url` as the origin without a trailing slash. Templates use Jekyll's URL filters throughout.

## Licenses

Original site code is under the [MIT license](LICENSE). The CV, lab logo, branding, and personal editorial content are excluded; see [content rights](CONTENT-LICENSE.md). Linked research outputs retain their own licenses.
