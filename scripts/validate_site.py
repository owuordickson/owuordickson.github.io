"""Validate the built site's public contract without third-party packages."""

import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])


def validate(root, base):
    routes = ["/", "/publications/", "/service/", "/teaching/", "/lab/"]
    assert root.is_dir(), f"Missing generated site: {root}"
    pages = {}
    for file in root.rglob("*.html"):
        pages[file.resolve()] = Page(file.read_text())
    for route in routes + ["/404.html"]:
        file = root / (route.lstrip("/") + ("index.html" if route.endswith("/") else ""))
        assert file.is_file(), f"Missing page: {route}"
        page = pages[file.resolve()]
        assert sum(tag == "h1" for tag, _ in page.tags) == 1, f"Expected one H1: {route}"
        assert any(tag == "title" for tag, _ in page.tags), f"Missing title: {route}"
        assert any(a.get("name") == "description" and a.get("content") for _, a in page.tags)
        canonical = [a["href"] for tag, a in page.tags if tag == "link" and a.get("rel") == "canonical"]
        assert canonical == ["https://owuordickson.github.io" + base + route], canonical
        nav = [a for _, a in page.tags if a.get("data-nav") == "true"]
        assert [a.get("href") for a in nav] == [base + r for r in routes], f"Navigation: {route}"
        assert sum(a.get("aria-current") == "page" for a in nav) == (0 if route == "/404.html" else 1)
        assert any(tag == "main" and a.get("id") == "main" for tag, a in page.tags)
    for file, page in pages.items():
        route = "/" + str(file.relative_to(root.resolve()))
        if route.endswith("index.html"):
            route = route[:-10]
        for tag, attrs in page.tags:
            if tag == "img":
                assert attrs.get("alt"), f"Missing image alternative: {file}"
            for key in ("href", "src"):
                if key not in attrs:
                    continue
                href = attrs[key]
                assert href, f"Empty URL: {file}"
                url = urlsplit(href)
                if url.scheme or url.netloc:
                    if href.startswith("https://doi.org/"):
                        assert re.match(r"^https://doi\.org/10\.\d{4,9}/\S+$", href), href
                    continue
                target = urlsplit(urljoin(base + route, href))
                assert not base or target.path.startswith(base + "/"), f"Missing baseurl: {href}"
                path = unquote(target.path[len(base):]).lstrip("/")
                resolved = root / path
                if resolved.is_dir():
                    resolved /= "index.html"
                assert resolved.is_file(), f"Broken local URL: {file.name}: {href}"
                if target.fragment and resolved.suffix == ".html":
                    assert unquote(target.fragment) in pages[resolved.resolve()].ids, f"Missing anchor: {href}"
    publications = pages[(root / "publications/index.html").resolve()]
    types = Counter(a["data-publication-type"] for _, a in publications.tags if "data-publication-type" in a)
    assert types == {"Journal article": 9, "International conference": 9, "National conference": 3, "Software": 2, "Dataset": 3}, types
    for private in ["Gemfile", "Gemfile.lock", "README.md", "LICENSE", "CONTENT-LICENSE.md", "scripts", "docs", "vendor", ".idea"]:
        assert not (root / private).exists(), f"Development file published: {private}"
    assert (root / "assets/documents/owuor.pdf").read_bytes().startswith(b"%PDF-")
    print(f"PASS: {len(pages)} pages, 26 publications, navigation, metadata, assets and internal links (baseurl={base!r})")


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve(), sys.argv[2].rstrip("/") if len(sys.argv) > 2 else "")
