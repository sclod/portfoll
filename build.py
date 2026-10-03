#!/usr/bin/env python3
"""Збирає статичний сайт з шаблонів у папку docs/ (для GitHub Pages).

Використання:
    python3 build.py
    SITE_URL=https://example.com/ python3 build.py
"""

import datetime
import hashlib
import os
import re
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markupsafe import Markup, escape

import content

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
OUT = ROOT / "docs"

# Абсолютна адреса сайту — потрібна для Open Graph і canonical.
SITE_URL = os.environ.get("SITE_URL", "https://sclod.github.io/portfoll/")


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:10]


def tech_terms() -> list[str]:
    """Назви технологій з контенту: «aiogram / Telegram Bot API» → «aiogram», «Telegram Bot API»."""
    raw = []
    for lang in content.LANGS:
        raw += [t for level in lang["stack"] for t in level["items"]]
        raw += [t for p in lang["projects"] for t in p["stack"]]
    terms = {"Telegram", "Claude"}
    for item in raw:
        for part in re.split(r"[,/]", re.sub(r"\(.*?\)", "", item)):
            part = part.strip()
            if part and not re.search(r"[а-яіїєґ]", part, re.I):
                terms.add(part)
    return sorted(terms, key=len, reverse=True)


# Підсвітка як у редакторі коду: колір означає тип, а не прикрасу.
# Порядок важливий — перше правило, що збіглося, виграє.
HIGHLIGHT_RULES = [
    ("str", ["у продакшені", "в проді", "дотепер", "in production", "present"]),
    ("kw", ["Strong Junior"]),
    ("type", ["ADMIN", "OPERATOR", "VIEWER"]),
    ("fn", tech_terms()),
]
_HL_CLASS = {}
_parts = []
for cls, words in HIGHLIGHT_RULES:
    for w in words:
        _HL_CLASS[w] = cls
        _parts.append(re.escape(str(escape(w))))
_parts.append(r"20\d\d")
HL_RE = re.compile(r"(?<![\w-])(" + "|".join(_parts) + r")(?!\w)")


def highlight(text: str) -> Markup:
    """Екранує текст і обгортає знайомі терміни в <span class="t-…">."""

    def wrap(m: re.Match) -> str:
        word = m.group(1)
        cls = _HL_CLASS.get(Markup(word).unescape(), "num")
        return f'<span class="t-{cls}">{word}</span>'

    return Markup(HL_RE.sub(wrap, str(escape(text))))


def code_lines(pairs) -> list[Markup]:
    """Словник Python для картки about.py: довгі списки — по два елементи на рядок."""

    def s(v: str) -> str:
        return f'<span class="t-str">"{escape(v)}"</span>'

    lines = ['<span class="t-var">developer</span> = {']
    for key, value in pairs:
        k = f'    <span class="t-key">"{escape(key)}"</span>: '
        if isinstance(value, str):
            lines.append(f"{k}{s(value)},")
        elif len(value) <= 2:
            lines.append(k + "[" + ", ".join(s(v) for v in value) + "],")
        else:
            lines.append(k + "[")
            for i in range(0, len(value), 2):
                lines.append("        " + ", ".join(s(v) for v in value[i : i + 2]) + ",")
            lines.append("    ],")
    lines.append("}")
    return [Markup(line) for line in lines]


def plural(n: int, forms: tuple[str, str, str]) -> str:
    """Множина за українськими правилами: 1 запис, 3 записи, 5 записів.
    Для англійської форми «few» і «many» однакові, тож правило підходить і їй."""
    one, few, many = forms
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
    env.filters["hl"] = highlight
    env.filters["code_lines"] = code_lines
    site_url = SITE_URL.rstrip("/") + "/"
    pages = {"uk": OUT / "index.html", "en": OUT / "en" / "index.html"}
    for lang in content.LANGS:
        code = lang["lang"]
        out = pages[code]
        out.parent.mkdir(parents=True, exist_ok=True)
        # Шлях від сторінки до кореня сайту — для CSS, шрифтів та іконок.
        root = "" if code == "uk" else "../"
        html = env.get_template("index.html").render(
            **lang,
            contacts=content.CONTACTS,
            root=root,
            site_url=site_url,
            page_url=site_url + ("" if code == "uk" else "en/"),
            alternates={"uk": site_url, "en": site_url + "en/"},
            year=datetime.date.today().year,
            # Версія для скидання кешу браузера після змін.
            css_v=file_hash(STATIC / "style.css"),
        )
        out.write_text(html, encoding="utf-8")
        print(f"Зібрано: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
