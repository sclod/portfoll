// Одноразова генерація PNG-картинок (Open Graph і іконки) у static/.
// Потрібні Node.js і Playwright з Chromium:  node tools/render_images.mjs
// Звичайна збірка сайту (build.py) цього не потребує — PNG уже лежать у static/.
import { chromium } from "playwright";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("..", import.meta.url));
const favicon = readFileSync(root + "static/favicon.svg", "utf8");

const og = `<!doctype html><html lang="uk"><meta charset="utf-8"><style>
  body { margin: 0; width: 1200px; height: 630px; background: #111316; color: #e4e6e9;
         font-family: system-ui, sans-serif; box-sizing: border-box; padding: 0 88px; display: flex; flex-direction: column; justify-content: center; }
  .mono { font-family: ui-monospace, "DejaVu Sans Mono", monospace; }
  h1 { font-size: 76px; margin: 0 0 24px; letter-spacing: -1.5px; line-height: 1.05; }
  p { font-size: 34px; line-height: 1.35; margin: 0 0 48px; max-width: 980px; }
  dl { display: grid; grid-template-columns: 1fr 1fr; column-gap: 48px; margin: 0; }
  dl div { display: grid; grid-template-columns: 150px 1fr; border-top: 2px solid #2c3137; padding: 18px 0; }
  dt { color: #9ba3ad; font-size: 22px; text-transform: uppercase; letter-spacing: 1px; padding-top: 6px; }
  dd { margin: 0; font-size: 30px; }
  .status { color: #5fcf8a; }
</style><body>
  <h1>Данііл Репецький</h1>
  <p>Роблю внутрішні системи для бізнесу — CRM, телеграм-боти, інтеграції, автоматизацію рутини.</p>
  <dl>
    <div><dt class="mono">Рівень</dt><dd>Strong Junior</dd></div>
    <div><dt class="mono">Місто</dt><dd>Київ</dd></div>
    <div><dt class="mono">База</dt><dd>Python, SQL</dd></div>
    <div><dt class="mono">CRM</dt><dd class="status">● у продакшені</dd></div>
  </dl>
</body></html>`;

const icon = (size) =>
  `<!doctype html><style>html,body{margin:0;background:transparent}svg{display:block;width:${size}px;height:${size}px}</style>${favicon}`;

const browser = await chromium.launch();
const page = await browser.newPage();

await page.setViewportSize({ width: 1200, height: 630 });
await page.setContent(og);
await page.screenshot({ path: root + "static/og.png" });

for (const [size, name] of [[32, "favicon-32.png"], [180, "apple-touch-icon.png"]]) {
  await page.setViewportSize({ width: size, height: size });
  await page.setContent(icon(size));
  await page.screenshot({ path: root + "static/" + name, omitBackground: true });
}

await browser.close();
console.log("Готово: static/og.png, static/favicon-32.png, static/apple-touch-icon.png");
