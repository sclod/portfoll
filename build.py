#!/usr/bin/env python3
"""Збирає статичний сайт з шаблонів у папку docs/ (для GitHub Pages).

Використання:
    python3 build.py
    SITE_URL=https://example.com/ python3 build.py
"""

import datetime
import hashlib
import os
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

import content

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT / "docs"

# Абсолютна адреса сайту — потрібна для Open Graph і canonical.
SITE_URL = os.environ.get("SITE_URL", "https://sclod.github.io/portfoll/")


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:10]


def plural(n: int, one: str, few: str, many: str) -> str:
    """Українська множина: 1 запис, 3 записи, 5 записів."""
    if n % 10 == 1 and n % 100 != 11:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


def build() -> None:
    # docs/*.md (дослідження, концепції) пишуться вручну — їх не чіпаємо.
    OUT.mkdir(exist_ok=True)
    for item in OUT.iterdir():
        if item.suffix == ".md":
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    shutil.copytree(STATIC, OUT, dirs_exist_ok=True)
    # Вимикає обробку Jekyll на GitHub Pages — файли віддаються як є.
    (OUT / ".nojekyll").touch()

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html"]),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["plural"] = plural
    html = env.get_template("index.html").render(
        site=content.SITE,
        contacts=content.CONTACTS,
        hero=content.HERO,
        projects=content.PROJECTS,
        stack=content.STACK,
        strengths=content.STRENGTHS,
        about=content.ABOUT,
        site_url=SITE_URL.rstrip("/") + "/",
        year=datetime.date.today().year,
        # Версії для скидання кешу браузера після змін.
        css_v=file_hash(STATIC / "style.css"),
        js_v=file_hash(STATIC / "theme.js"),
    )
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print(f"Зібрано: {OUT.relative_to(ROOT)}/index.html")


if __name__ == "__main__":
    build()
