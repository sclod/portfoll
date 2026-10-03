// Одноразова генерація PNG-картинок (Open Graph і іконки) у static/.
// Потрібні Node.js і Playwright з Chromium:  node tools/render_images.mjs
// Звичайна збірка сайту (build.py) цього не потребує — PNG уже лежать у static/.
import { chromium } from "playwright";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("..", import.meta.url));
const favicon = readFileSync(root + "static/favicon.svg", "utf8");

const og = `<!doctype html><html lang="uk"><meta charset="utf-8"><style>
  body { margin: 0; width: 1200px; height: 630px; background: #0e1116; color: #e7e9ec;
         font-family: system-ui, sans-serif; display: flex; flex-direction: column;
         justify-content: center; padding: 0 88px; box-sizing: border-box;
         border-top: 10px solid #4fd1a5; }
  .eyebrow { font-family: ui-monospace, "DejaVu Sans Mono", monospace; color: #4fd1a5; font-size: 30px; margin-bottom: 28px; }
  h1 { font-size: 84px; margin: 0 0 32px; letter-spacing: -2px; line-height: 1.05; }
  p { font-size: 36px; line-height: 1.35; color: #a1aab6; margin: 0; max-width: 980px; }
  .foot { position: absolute; left: 88px; bottom: 56px; font-family: ui-monospace, "DejaVu Sans Mono", monospace; font-size: 26px; color: #a1aab6; }
</style><body>
  <div class="eyebrow">Розробник · Strong Junior · Київ</div>
  <h1>Данііл Репецький</h1>
  <p>Внутрішні системи для бізнесу: CRM, телеграм-боти, інтеграції, автоматизація рутини.</p>
  <div class="foot">Python · SQL · Telegram · Linux</div>
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
