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

---

# Раунд 2: как люди делают портфолио на самом деле

Запрос: сайт для Strong Junior получился слишком «мощным». Нужно посмотреть ~15 реальных сайтов
и сделать проще, компактнее, с капелькой космоса.

**Метод.** Сайты-галереи (awwwards, onepagelove, siteinspire) и сами портфолио сетевая политика
сессии не пускает. Зато доступен GitHub. Взял известный список
[emmabostian/developer-portfolios](https://github.com/emmabostian/developer-portfolios) (267 сайтов на github.io),
склонировал 24 случайных репозитория `user.github.io` со статическим HTML и открыл их локально в Chromium.
Нормально отрисовались 21; три пустые или без стилей
([aditya113141](https://aditya113141.github.io), [akashblsbrmnm](https://akashblsbrmnm.github.io), [narender24681](https://narender24681.github.io)).

## Что повторяется почти у всех

- **Большой первый экран с фото и «Hi, I'm …».** [lionelsamrat10](https://lionelsamrat10.github.io),
  [omchaudhari1107](https://omchaudhari1107.github.io), [lakshanrukantha](https://lakshanrukantha.github.io),
  [krash-cod3](https://krash-cod3.github.io), [pankaj-kumar-techie](https://pankaj-kumar-techie.github.io),
  [sreegodavarthi](https://sreegodavarthi.github.io), [oussamabouchikhi](https://oussamabouchikhi.github.io).
  Первый экран целиком уходит на имя и фото, информации ноль.
- **Печатающийся текст с курсором.** krash-cod3, lakshanrukantha, omchaudhari1107.
- **Неон, свечения, тяжёлые фоны.** pankaj-kumar-techie, [neelanjan-chakraborty](https://neelanjan-chakraborty.github.io),
  [cuierd](https://cuierd.github.io) (сеть из линий), [iglesiaskevinralphbusiness](https://iglesiaskevinralphbusiness.github.io).
- **Кнопки «Hire me» / «Download CV»** и полоски навыков в процентах ([andredfaria](https://andredfaria.github.io)).

## Что читается быстрее всего

- **Формат резюме: даты слева, суть справа.** [andredfaria](https://andredfaria.github.io) — плотно,
  без лишнего, всё видно за минуту прокрутки.
- **Минимум оформления.** [mouadziani](https://mouadziani.github.io) — моноширинный шрифт, короткие секции,
  никаких эффектов; [machado001](https://machado001.github.io) — одна фраза и кнопка.
- **Бэкенд-разработчик о себе одной фразой.** [devravik](https://devravik.github.io): «большую часть времени
  делаю multi-tenant SaaS и внутренние инструменты» + список «чем занимаюсь». Ближе всего к нашему случаю.
- **Чистая светлая подача с одной сильной фразой.** [aniketksh](https://aniketksh.github.io).

## Космос, который работает

- [eckeecke](https://eckeecke.github.io) и [crackedontiti](https://crackedontiti.github.io): тёмный фон
  с редкими звёздами, контент спокойно поверх. Космос — фон и настроение, а не главный объект.
  Это и есть «совсем немного космоса».

## Решения

1. Одна колонка ~780px. Записи как в резюме: период и статус слева, проект справа.
2. Никакого фото, печатающегося текста, 3D и огромных заголовков. Первый экран: одна фраза, две строки о себе, кнопка.
3. Космос: звёздное небо на фоне (три слоя, медленное мерцание), одна небольшая планета у заголовка,
   комета раз в ~16 секунд. Всё на CSS, `prefers-reduced-motion` выключает движение.
4. Шрифты: Manrope + JetBrains Mono. Декоративный Unbounded убран (минус ~80 КБ).
