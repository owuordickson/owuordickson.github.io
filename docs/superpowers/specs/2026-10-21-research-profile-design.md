# Research profile and Owuor Lab website

Status: design approved in conversation; written specification awaiting review.

## Purpose and audience

Build Dickson Odhiambo Owuor's public academic profile and Owuor Lab website in this repository using Jekyll. The intended audience is research collaborators, prospective students, academic peers, and students looking for teaching information. Deliver the implementation as a pull request to `owuordickson/owuordickson.github.io`.

## Approved direction

A custom, lightweight, responsive Jekyll layout with five persistent navigation links: About, Publications, Service, Teaching, and Owuor Lab. Use a restrained green and charcoal palette drawn from the supplied logo, generous whitespace, readable typography, and an academic editorial style. A standard theme was considered; the custom layout was selected to give the personal profile and lab a consistent identity.

## Sources and factual boundaries

Use the supplied `owuor.pdf` CV as the source for biography, education, research, publications, service, teaching, and supervision. Use the supplied `owlab-green.png` as the lab logo. Both files are available locally; copy the public assets into the repository during implementation. Include a downloadable copy of the supplied CV. Do not publish the postal address, phone number, or membership identifiers in page content. Use the professional contact email and GitHub profile supplied in the CV.

Do not invent lab members, lab affiliations, recruitment openings, project outcomes, course links, paper links, or news. Describe lab research themes using the documented research record without asserting that every collaborator or supervised student is a lab member. Treat dated appointments and supervision records as CV information, rather than guessing changes since the CV was written. Omit undated bibliometric counters: they become stale and are unnecessary to the site.

## Information architecture

### About (`/`)

Lead with the name Dickson Odhiambo Owuor, the Senior Lecturer role at Strathmore University recorded in the CV, and a concise description of data-centric knowledge discovery. Present research interests as a small number of readable themes: gradual pattern mining and time series; knowledge representation and graphs; learning for scientific and surveillance applications. Include education, selected research software (`so4gp`, `sgtlib`), professional contact, GitHub, and a CV download. Present appointments with their recorded date ranges where relevant.

### Publications (`/publications/`)

Include all 26 entries listed in the CV: nine journal articles, nine international conference entries, three national conference entries, two software releases, and three datasets. Group entries by year in descending order and label their publication type and venue. Preserve authors and titles, render accents correctly, and provide DOI or source links only when supplied. Avoid importing quartile rankings and citation counts. Store records in `_data/publications.yml` so adding a paper does not require editing templates.

### Service (`/service/`)

Distinguish program committee membership from reviewing. Include CARI PC membership (2024-2026), IPMU reviewing (2026), KDIR reviewing (2021), and the six journals named in the CV. Include VIP coordination, partnerships work, and professional memberships without membership numbers. Store structured service entries in `_data/service.yml`.

### Teaching (`/teaching/`)

Describe undergraduate and graduate teaching and list the documented subject areas: programming, object-oriented programming, embedded systems and IoT, distributed systems, and data mining, storage and retrieval. Do not attach invented course codes, dates, syllabi, or learning materials. Include documented completed and ongoing doctoral supervision, clearly separated and retaining the source's tentative completion dates where shown. Do not repeat the biography's inconsistent claim of three ongoing PhDs; the detailed CV lists two. Store courses and supervision in `_data/teaching.yml`.

### Owuor Lab (`/lab/`)

Feature the supplied logo with descriptive alternative text and its natural aspect ratio. Introduce the lab through research themes grounded in the CV: gradual patterns; graph-based microscopy analysis; knowledge graphs; disease surveillance; reinforcement learning and bioinformatics. Link the documented research software and provide an email contact for research enquiries. Do not add a fabricated team directory or imply a formal institutional lab affiliation.

## Implementation structure

Use a shared HTML layout in `_layouts/`, navigation and reusable fragments in `_includes/`, YAML records in `_data/`, Markdown pages for narrative content, and a single maintained stylesheet under `assets/css/`. Keep the logo and CV under `assets/`. Navigation entries come from a central data file, with a clear active-page state.

Use Jekyll with a Gemfile and lockfile, GitHub Pages-compatible plugins only if necessary, and a documented local preview command. Set the canonical URL to `https://owuordickson.github.io` and default `baseurl` to the empty string. Generate internal URLs with Jekyll's `relative_url` and canonical URLs with `absolute_url`. Include page titles, descriptions, canonical links, a favicon derived from the branding if practical, and a useful 404 page. Do not require a database, application server, analytics service, remote font service, or JavaScript for core navigation and content.

## Visual and accessibility behavior

Use a light background, charcoal text, and dark green accents with sufficient contrast. Keep prose to a comfortable reading width and give publication lists enough space for long titles. The header must fit at narrow widths using wrapping or a simple accessible responsive arrangement. Use semantic landmarks, one primary heading per page, a keyboard-visible skip link, visible focus styles, accessible link names, and `aria-current` on the active navigation link. Respect reduced-motion preferences if motion is introduced. Maintain readability at mobile and desktop widths without horizontal overflow.

## Build and maintenance

Add a GitHub Actions workflow that builds the site for pull requests. Enable GitHub Pages artifact deployment only from the default branch, with minimal permissions and environment protection. Document that the repository's Pages source must be GitHub Actions before first deployment. Exclude design documents, build dependencies, and local development files from the generated site. Preserve the existing untracked `.idea/` directory and exclude IDE files from version control.

The README must explain installation, local preview, validation, deployment setup, and how to update each data file. No secrets or personal local paths should be embedded in the generated site.

## Validation and acceptance

1. Install the declared dependencies and run a production Jekyll build with strict front matter checking.
2. Confirm all five navigation destinations, 404 page, CSS, logo, and CV download resolve in the generated output.
3. Validate publication counts, required metadata, DOI formatting, and internal links; verify the output with both empty and non-empty base paths.
4. Inspect the rendered pages at mobile and desktop sizes, including the longest publication entries and the lab logo.
5. Check keyboard navigation, active link states, headings, image alternatives, and obvious accessibility issues.
6. Review the final content against the supplied CV and ensure there are no invented claims, placeholder content, or unintended personal identifiers.
7. Open a pull request summarizing the resulting behavior, validation performed, and any remaining deployment configuration needed from the repository owner. Creating the PR is authorized; merging it is outside this request.

## Scope limits

No blog, CMS, dynamic publication API, search, student portal, tracking, contact form backend, or external hosting platform is required. The site should remain easy to maintain through Markdown and YAML in GitHub.
