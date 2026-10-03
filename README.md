# portfoll

Особистий сайт-портфоліо. Одна сторінка, статичний HTML, роздається через GitHub Pages з папки `docs/`.

## Структура

- `content.py` — увесь текст сайту (проєкти, стек, контакти)
- `templates/index.html` — шаблон Jinja2
- `static/` — CSS, переключатель теми, іконки, Open Graph картинка; копіюється в `docs/` як є
- `build.py` — збирає `docs/`
- `tools/render_images.mjs` — необов'язково: перегенерувати `og.png` та PNG-іконки (Node.js + Playwright)

## Збірка

```sh
pip install -r requirements.txt
python3 build.py
```

Результат — у `docs/`. Після змін у `content.py`, шаблоні чи `static/` запусти збірку й закоміть `docs/` разом зі змінами.

Адреса сайту для Open Graph і canonical за замовчуванням — `https://sclod.github.io/portfoll/`. Інша адреса: `SITE_URL=https://example.com/ python3 build.py`.

## Публікація

GitHub → Settings → Pages → Source: *Deploy from a branch*, гілка `main`, папка `/docs`.
