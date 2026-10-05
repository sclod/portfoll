// Одноразова генерація PNG-картинок (Open Graph і іконки) у static/.
// Потрібні Node.js і Playwright з Chromium:  node tools/render_images.mjs
// Звичайна збірка сайту (build.py) цього не потребує — PNG уже лежать у static/.
import { chromium } from "playwright";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("..", import.meta.url));
const favicon = readFileSync(root + "static/favicon.svg", "utf8");

// Шрифти вбудовуються як data: URL — Chromium не вантажить шрифти з file://.
const font = (family, file, weight) => {
  const data = readFileSync(root + "static/fonts/" + file).toString("base64");
  return `@font-face { font-family: "${family}"; font-weight: ${weight}; src: url(data:font/woff2;base64,${data}) format("woff2"); }`;
};
const fonts = [
  font("Manrope", "manrope-cyrillic.woff2", "400 700"), font("Manrope", "manrope-latin.woff2", "400 700"),
  font("JetBrains Mono", "jetbrains-mono-cyrillic.woff2", "400 600"), font("JetBrains Mono", "jetbrains-mono-latin.woff2", "400 600"),
].join("\n");

const planet = favicon.replace(/<rect[^>]*\/>/, "").replace(/<circle cx="(12|52|50)"[^>]*\/>/g, "");

const og = (t) => `<!doctype html><html lang="${t.lang}"><meta charset="utf-8"><style>${fonts}
  body { margin: 0; width: 1200px; height: 630px; overflow: hidden; position: relative; color: #e8eaf2;
         background: radial-gradient(ellipse 55% 70% at 88% 0%, rgba(124,92,255,.42), transparent 70%), radial-gradient(ellipse 45% 60% at 5% 0%, rgba(56,104,255,.3), transparent 70%), radial-gradient(ellipse 35% 40% at 70% 70%, rgba(40,210,200,.12), transparent 70%), #07080f;
         font-family: "Manrope", sans-serif; box-sizing: border-box; padding: 0 90px; display: flex; flex-direction: column; justify-content: center; }
  h1 { font-size: 76px; font-weight: 700; line-height: 1.08; letter-spacing: -2px; margin: 0 0 28px; }
  h1 span { display: block; background: linear-gradient(90deg, #a9b6ff, #c7a8ff); -webkit-background-clip: text; color: transparent; }
  p { font-size: 32px; margin: 0; color: #c3c8d6; font-weight: 500; }
  .fn { font-family: "JetBrains Mono", monospace; color: #93b2ff; font-size: .9em; }
  svg { position: absolute; right: 110px; top: 120px; width: 230px; height: 230px; filter: drop-shadow(0 0 40px rgba(140,120,255,.45)); }
</style><body>${planet}
  <h1>${t.h1a} <span>${t.h1b}</span></h1>
  <p>${t.text}</p>
</body></html>`;

// Тексти — ті самі, що в content.py (h1, lead).
const ogTexts = [
  { file: "og.png", lang: "uk", h1a: "Внутрішні системи", h1b: "для бізнесу",
    text: 'CRM, телеграм-боти, інтеграції. База — <span class="fn">Python</span> і <span class="fn">SQL</span>.' },
  { file: "og-en.png", lang: "en", h1a: "Internal systems", h1b: "for business",
    text: 'CRM, Telegram bots, integrations. Core: <span class="fn">Python</span> and <span class="fn">SQL</span>.' },
];

const icon = (size) =>
  `<!doctype html><style>html,body{margin:0;background:transparent}svg{display:block;width:${size}px;height:${size}px}</style>${favicon}`;

const browser = await chromium.launch();
const page = await browser.newPage();

await page.setViewportSize({ width: 1200, height: 630 });
for (const t of ogTexts) {
  await page.setContent(og(t));
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: root + "static/" + t.file });
}

for (const [size, name] of [[32, "favicon-32.png"], [180, "apple-touch-icon.png"]]) {
  await page.setViewportSize({ width: size, height: size });
  await page.setContent(icon(size));
  await page.screenshot({ path: root + "static/" + name, omitBackground: true });
}

await browser.close();
console.log("Готово: static/og.png, static/og-en.png, static/favicon-32.png, static/apple-touch-icon.png");
