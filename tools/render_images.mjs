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
  font("Unbounded", "unbounded-cyrillic.woff2", "500 800"), font("Unbounded", "unbounded-latin.woff2", "500 800"),
  font("Manrope", "manrope-cyrillic.woff2", "400 700"), font("Manrope", "manrope-latin.woff2", "400 700"),
  font("JetBrains Mono", "jetbrains-mono-cyrillic.woff2", "400 600"), font("JetBrains Mono", "jetbrains-mono-latin.woff2", "400 600"),
].join("\n");

const og = `<!doctype html><html lang="uk"><meta charset="utf-8"><style>${fonts}
  body { margin: 0; width: 1200px; height: 630px; overflow: hidden; position: relative; background: #07090d; color: #e9edf4;
         font-family: "Manrope", sans-serif; box-sizing: border-box; padding: 0 80px; display: flex; flex-direction: column; justify-content: center; }
  body::before { content: ""; position: absolute; inset: 0; z-index: -1;
         background: radial-gradient(circle at 10% 0%, rgba(79,224,240,.18), transparent 45%), radial-gradient(circle at 95% 100%, rgba(185,140,255,.2), transparent 50%),
                     radial-gradient(rgba(160,180,210,.13) 1px, transparent 1.4px) 0 0 / 26px 26px; }
  .c { font-family: "JetBrains Mono", monospace; color: #8591a6; font-size: 26px; margin-bottom: 22px; }
  h1 { font-family: "Unbounded", sans-serif; font-size: 80px; font-weight: 700; line-height: 1.04; letter-spacing: -2px; margin: 0 0 30px; }
  h1 span { display: block; background: linear-gradient(100deg, #4fe0f0, #7aa7ff 45%, #b98cff); -webkit-background-clip: text; color: transparent; }
  p { font-size: 32px; line-height: 1.4; margin: 0; max-width: 700px; font-weight: 500; }
  b { font-weight: 700; background: linear-gradient(100deg, #4fe0f0, #b98cff) no-repeat 0 100% / 100% 3px; }
  .fn { font-family: "JetBrains Mono", monospace; color: #82adff; font-size: .9em; }
  .scene { position: absolute; right: 120px; top: 50%; width: 200px; height: 200px; margin-top: -100px; perspective: 900px; }
  .cube { width: 200px; height: 200px; position: relative; transform-style: preserve-3d; transform: rotateX(-24deg) rotateY(-38deg); }
  .f { position: absolute; inset: 0; display: grid; place-items: center; border: 1.5px solid rgba(122,200,255,.6); border-radius: 8px;
       background: linear-gradient(135deg, rgba(79,224,240,.25), rgba(185,140,255,.16)), rgba(14,19,27,.75);
       font-family: "Unbounded", sans-serif; font-size: 34px; font-weight: 700; box-shadow: inset 0 0 40px rgba(79,224,240,.2); }
  .f1 { transform: translateZ(100px); } .f2 { transform: rotateY(90deg) translateZ(100px); } .f3 { transform: rotateX(90deg) translateZ(100px); }
  .ring { position: absolute; left: -110px; top: -110px; width: 420px; height: 420px; border: 1.5px solid rgba(79,224,240,.35); border-radius: 50%; transform: rotateX(74deg) rotateY(-8deg); }
</style><body>
  <div class="c">// розробник · Київ</div>
  <h1>Данііл <span>Репецький</span></h1>
  <p>Роблю <b>внутрішні системи для бізнесу</b>. База — <span class="fn">Python</span> і <span class="fn">SQL</span>.</p>
  <div class="scene"><div class="ring"></div><div class="cube"><div class="f f1">CRM</div><div class="f f2">BOT</div><div class="f f3">SQL</div></div></div>
</body></html>`;

const icon = (size) =>
  `<!doctype html><style>html,body{margin:0;background:transparent}svg{display:block;width:${size}px;height:${size}px}</style>${favicon}`;

const browser = await chromium.launch();
const page = await browser.newPage();

await page.setViewportSize({ width: 1200, height: 630 });
await page.setContent(og);
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: root + "static/og.png" });

for (const [size, name] of [[32, "favicon-32.png"], [180, "apple-touch-icon.png"]]) {
  await page.setViewportSize({ width: size, height: size });
  await page.setContent(icon(size));
  await page.screenshot({ path: root + "static/" + name, omitBackground: true });
}

await browser.close();
console.log("Готово: static/og.png, static/favicon-32.png, static/apple-touch-icon.png");
