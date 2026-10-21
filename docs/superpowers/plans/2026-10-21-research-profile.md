# Research Profile Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan inline. The user explicitly requested immediate implementation after approving the spec.

**Goal:** Deliver the five-page Jekyll research profile and Owuor Lab site as a pull request.

**Architecture:** Markdown pages share a semantic Liquid layout and a responsive CSS stylesheet. YAML data holds navigation, publications, service, and teaching. GitHub Actions validates root and subpath builds and deploys only from main.

**Tech Stack:** Jekyll 4.4, Ruby, Liquid, CSS, Python standard-library output validation, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-10-21-research-profile-design.md`

## Global Constraints

- Five tabs: About, Publications, Service, Teaching, Owuor Lab.
- Use only documented CV facts; include all 26 listed publications.
- No application server, remote fonts, analytics, or JavaScript required for core content.
- All internal links support a non-empty baseurl.
- Preserve existing IDE files locally; ignore them in Git and exclude non-site files from output.
- MIT applies to original site code; CV, branding, and personal editorial material remain reserved.

## Review Focus

- Long citations and navigation at 375px must wrap without overflow.
- Nested base paths must preserve navigation, CSS, logo, and download links.
- Papers without supplied URLs must render complete citations without empty links.
- PR workflows must validate without Pages credentials or write permissions.
- CV supervision totals conflict; use the detailed lists of three completed and two ongoing doctoral projects.

### Task 1: Site foundation and content

**Files:** `.gitignore`, `LICENSE`, `CONTENT-LICENSE.md`, `Gemfile`, `Gemfile.lock`, `.ruby-version`, `_config.yml`, `_layouts/default.html`, `_includes/navigation.html`, `_data/*.yml`, `index.md`, `publications.html`, `service.html`, `teaching.html`, `lab.md`, `404.html`, `assets/css/main.css`, `assets/images/owlab-green.png`, `assets/documents/owuor.pdf`, `scripts/validate_site.py`.

**Interfaces:** YAML supplies string metadata and typed publication years to Liquid; generated output supplies HTML and assets to the validation script. The validator takes output directory and optional baseurl as command-line arguments.

- [x] Write output validation for five pages, navigation, one H1, title/description/canonical, publication count/types, DOI links, local assets and fragment targets. Run against the empty repository and observe missing-output failure.
- [x] Create the Jekyll build, reusable templates, five pages, CV-derived YAML, original CSS, branding, exclusions, and licenses.
- [x] Install dependencies, build with strict front matter, and run validation. Expected: 26 publications, complete internal links, all pages valid.
- [x] Build with `/preview` baseurl and validate that output. Expected: no missing or incorrectly prefixed local URLs.

### Task 2: Delivery and verification

**Files:** `.github/workflows/pages.yml`, `README.md`, documentation status updates.

**Interfaces:** Workflow uses the same locked bundle, build command, and validator from Task 1. README documents those exact commands and data schemas.

- [x] Add PR validation and main-only Pages deployment with narrowly scoped job permissions.
- [x] Document Ruby setup, local preview, content maintenance, licensing, validation, and first deployment settings.
- [x] Inspect every page at desktop and mobile sizes; check logo, long citations, keyboard navigation, and overflow.
- [x] Run final root/subpath validation and `git diff --check`; review the entire diff against the spec.
- [ ] Commit, push the feature branch, and create the requested PR with a concrete description and validation evidence. Do not merge or change hosting settings.

## Execution record

- Implemented inline as explicitly requested; used the existing feature branch and preserved local IDE files.
- The initial output validator failed because no generated site existed, then passed against the implementation.
- Strict production and `/preview` builds passed; each validated six pages, all 26 publications, internal links, metadata, and local assets.
- Isolated browser checks passed for all six routes at 320, 375, 768, and 1440px: no horizontal overflow, broken images, empty links, or page errors; keyboard skip navigation reached main content.
- Inspected desktop and mobile screenshots of the About, Publications, and Lab pages. The supplied PNG renders with transparency and correct proportions.
- Independent whole-site review found no Critical or Important issues. Corrected two minor content presentation details: neutral formatting for article identifiers and exact supervisor surnames from the detailed CV.
- Ruby 3.4 dependency lock supports macOS and Linux. The local preview server is available at `http://127.0.0.1:4000` during this session.
- MIT covers original site code; personal content and lab branding are explicitly excluded.
