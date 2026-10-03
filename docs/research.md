# Исследование: портфолио разработчиков

Один проход, 12 запросов из лимита в 15. К этому файлу больше не возвращаемся.

**Ограничение среды.** Сетевая политика облачной сессии блокирует прямые заходы на сайты.
Не открылись: brittanychiang.com, leerob.com, rauno.me, danluu.com, mitchellh.com (5 запросов ушли впустую).
Поэтому выводы ниже собраны по выдаче поиска и по разборам этих сайтов из каталогов, а не по самим страницам.
Если где-то нужна точность «как оно выглядит сегодня», это надо перепроверить вручную.

## 1. Что повторяется у всех — делать НЕ надо

- **Клон Brittany Chiang v4.** Тёмно-синий фон, мятный акцент, нумерованные секции «01. About», боковая
  рельса с иконками соцсетей. Это самое копируемое портфолио в сети: тысячи форков с 2020 года.
  → [onepagelove](https://onepagelove.com/brittany-chiang), [форк-пример](https://github.com/pycoder2000/portfolio-v4), [GitHub topic](https://github.com/topics/brittanychiang)
- **Hero-шаблон.** Огромное имя, расплывчатая строка «I build things for the web», кнопка. По наблюдению
  студии: «стоковая картинка, расплывчатый заголовок и подзаголовок, который ничего не говорит».
  → [lineanddotstudio](https://lineanddotstudio.com/blog/website-design-trends-2026/)
- **Шкалы навыков «JavaScript 85%».** Прямо названы любительскими.
  → [hakia](https://hakia.com/skills/building-portfolio/)
- **Сетка карточек-скриншотов.** Плитки 2×2 или 3×N, превью, теги-«таблетки», ссылки «Live / Code».
  Это стандарт всех шаблонов из подборок.
  → [colorlib](https://colorlib.com/wp/developer-portfolios/), [myseera](https://myseera.com/blog/best-developer-portfolio-templates-2026)
- **Glassmorphism, градиентные пятна, фиолетовый акцент.** Один и тот же «generic»-вид, потому что все
  вдохновляются одними и теми же галереями.
  → [lineanddotstudio](https://lineanddotstudio.com/blog/website-design-trends-2026/)
- **Терминал-портфолио.** Фейковая консоль, `$ whoami`, печатающийся текст. Давно отдельный жанр с
  десятками шаблонов, то есть уже не оригинально. Плюс это плохо для доступности и для того, кто просто хочет прочитать.
  → [GitHub topic terminal-website](https://github.com/topics/terminal-website), [dev.to](https://dev.to/nahiancdx/few-amazing-terminal-style-portfolio-website-you-might-like-4pom)
- **Тренды-2026 как цель**: 3D на WebGPU, AI-чат-бот на сайте, геймификация. Для backend/internal-разработчика
  это шум, который ничего не говорит о его работе.
  → [envato](https://elements.envato.com/learn/portfolio-trends), [learni](https://learni-group.com/en/blog/how-to-build-developer-portfolio-website-march-2026)
- **Много тонких учебных проектов.** «Десять клонов из туториалов выглядят хуже двух настоящих».
  → [hakia](https://hakia.com/skills/building-portfolio/)

## 2. Что встречается редко и работает

- **Почти чистый текст.** У Paco Coursey монохром, плоско, иерархия задаётся размером и отступами,
  а не цветом и тенями; работа говорит сама за себя. Редкость именно в сдержанности.
  → [opendesign: Paco](https://opendesign.cc/en/sites/paco), [portfolioproject](https://portfolioproject.io/website/paco-coursey), [scrimba](https://scrimba.com/articles/web-developer-portfolio-inspiration/)
- **Сайт как документ, а не как витрина.** Колофон («как сделан этот сайт»), /now, /uses: страницы,
  которые описывают человека и инструменты прямо, без маркетинга.
  → [IndieWeb: colophon](https://indieweb.org/colophon), [IndieWeb: now](https://indieweb.org/now), [hedy.dev](https://home.hedy.dev/posts/meta-pages/)
- **Форма, взятая из собственной работы автора** (газетный «Paper Portfolio» у дизайнера, который
  работает с печатью). Работает, когда метафора честная, и превращается в гиммик, когда нет.
  → [scrimba](https://scrimba.com/articles/web-developer-portfolio-inspiration/)
- **Для backend-ролей**: решения и компромиссы важнее картинок. Логи, мониторинг, деплой, «почему так»
  показывают инженерную зрелость. Формат: одно предложение «что и зачем», затем детали.
  → [foliox](https://foliox.me/portfolio-for/backend-developers), [dev.to checklist](https://dev.to/_d7eb1c1703182e3ce1782/developer-portfolio-checklist-20-things-hiring-managers-look-for-388p)

## 3. Как подают проекты с закрытым кодом

- **Описывать возможности и архитектуру, а не внутренности.** Что система умеет, какие проблемы решены,
  как устроена эксплуатация. Это инженерия, а не тайна клиента.
  → [hassanjaved.work](https://www.hassanjaved.work/blog/working-under-nda-freelance-engineer-guide)
- **Явно помечать, что код закрыт.** Это показывает, что человек уважает договорённости.
  Но один заголовок с пометкой «NDA» без содержания — плохой опыт для читателя: лучше не показывать совсем.
  → [freelancermap](https://www.freelancermap.com/blog/can-i-share-nda-protected-work-on-my-portfolio-tips-and-advice/), [meetharlow](https://meetharlow.com/blog/how-to-build-a-portfolio-when-your-best-wins-are-locked-by-ndas/)
- **Санитизированный клон с выдуманными данными** рядом с закрытым проектом: «боевой код закрыт, вот
  открытая версия того же класса задач». VehicleFlow Demo уже ровно это.
  → [skillhub](https://skillhub.com/blog/digital-portfolio-building-under-nda), [medium/portfolio-principles](https://medium.com/portfolio-principles/how-to-show-nda-protected-work-on-your-online-portfolio-2fefa5809d01)
- **Обезличивание и выдуманные данные** с дисклеймером, если нужна визуализация.
  → [ixdf](https://ixdf.org/literature/article/keep-it-confidential-how-to-showcase-your-nda-protected-design-work)

## Выводы для нашего сайта

1. Никаких скриншотов-плиток, «таблеток» тегов, процентов навыков, фейкового терминала и мятного акцента на тёмно-синем.
2. Проект подаётся как **описание системы**: назначение → функции → состояние → стек → доступ к коду.
   Для CRM строка «Код закрытий — лише опис» стоит прямо в карточке, рядом с богатым списком возможностей.
3. VehicleFlow подписан как санитизированная версия: это и есть «открытый клон» из пункта 3.
4. Форма сайта берётся из того, что человек реально строит: записи, поля, статусы, журналы. Но без фейковых
   метрик и графиков: цифр в брифе нет, значит и на странице их не будет.
5. Сдержанность: один акцент, а цвет только там, где он что-то значит (статус).
