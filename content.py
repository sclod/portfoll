"""Увесь текст сайту — українською (UK) та англійською (EN).
Редагуй тут, потім запусти `python3 build.py`.

Порожні поля ("" або []) на сторінці не виводяться — нічого не треба вигадувати, щоб заповнити.
Структура UK і EN однакова: що додаєш в одну мову, додай і в іншу.
"""

CONTACTS = {
    "telegram": {"label": "Telegram", "handle": "@D0SIDE0", "url": "https://t.me/D0SIDE0"},
    "github": {"label": "GitHub", "handle": "github.com/sclod", "url": "https://github.com/sclod"},
}

# Стек проєктів однаковий для обох мов.
CRM_STACK = ["PostgreSQL", "Telegram Bot API", "Linux", "Nginx", "PM2", "TypeScript (AI-assisted)"]
VF_STACK = ["Next.js", "TypeScript", "Prisma", "SQLite", "Leaflet", "Playwright (E2E)"]
BOTS_STACK = ["Python", "aiogram", "Telegram Bot API", "PostgreSQL", "SQLite", "REST API"]
VF_CODE_URL = "https://github.com/sclod/vehicleflow-demo"
SWAP_STACK = ["Next.js", "TypeScript", "Prisma", "SQLite", "Socket.IO", "Zod", "Tailwind CSS"]
SWAP_CODE_URL = "https://github.com/sclod/swapdesk"

# Поля проєкту (усі, крім title і glyph, необов'язкові):
#   glyph     — коротка декоративна позначка на фоні картки
#   period    — період
#   status    — {"label": ..., "kind": "prod" | "demo"}
#   purpose   — призначення / у чому задача
#   functions — що побудовано
#   challenge — що було складним
#   result    — що вийшло
#   code      — {"text": ..., "url": ...}
#   stack     — список технологій

UK = {
    "lang": "uk",
    "locale": "uk_UA",
    "site": {
        "title": "Внутрішні системи для бізнесу — CRM, телеграм-боти, інтеграції",
        "description": (
            "Розробник з Києва. Роблю внутрішні системи для бізнесу — CRM, "
            "телеграм-боти, інтеграції, автоматизацію рутини. База — Python і SQL."
        ),
        "og_alt": "Внутрішні системи для бізнесу: CRM, телеграм-боти, інтеграції.",
    },
    "ui": {
        "skip": "Перейти до вмісту",
        "home": "На початок",
        "brand": "портфоліо",
        "nav_label": "Розділи сторінки",
        "nav": {
            "projects": "Проєкти",
            "stack": "Стек",
            "strengths": "Сильні сторони",
            "about": "Про мене",
            "contacts": "Контакти",
        },
        "lang_switch": {"label": "EN", "title": "English version", "href": "en/", "hreflang": "en"},
        "kicker": "// розробник · Strong Junior · Київ",
        "h1": ["Внутрішні системи", "для бізнесу"],
        "cta": "Написати",
        "cta_sr": "в Telegram",
        "records": ("запис", "записи", "записів"),
        "stack_label": "// від фундаменту до надбудови",
        "strengths_label": "// як я працюю",
        "about_label": "// коротко",
        "contacts_label": "// зв'язок",
        "built": "Що зроблено",
        "challenge": "Що було складним",
        "result": "Результат",
        "code": "Код",
        "code_link": "Код на GitHub",
        "log": "Журнал",
    },
    "hero": {
        "lead": "CRM, телеграм-боти, інтеграції, автоматизація рутини.",
        "text": (
            "База — Python і SQL. Веб-частину пишу з активним використанням "
            "AI-інструментів: ставлю задачу, перевіряю результат, дебажу, відповідаю "
            "за те, як воно працює в проді."
        ),
        # Картка «about.py» у першому екрані: ключ → рядок або список рядків.
        "code": [
            ("рівень", "Strong Junior"),
            ("місто", "Київ"),
            ("база", ["Python", "SQL"]),
            ("робить", ["CRM", "телеграм-боти", "інтеграції", "автоматизація рутини"]),
            ("зв'язок", "@D0SIDE0"),
        ],
    },
    "projects": [
        {
            "title": "CRM для юридичної практики",
            "glyph": "CRM",
            "period": "2023 — дотепер",
            "status": {"label": "У продакшені", "kind": "prod"},
            "purpose": "Внутрішня система, зроблена з нуля, підтримується мною.",
            "functions": [
                "Картки клієнтів, документи, задачі, нагадування про строки договорів",
                "Рольова модель ADMIN / OPERATOR / VIEWER з розмежуванням доступу",
                "Журнал дій користувачів та історія змін по кожній картці",
                "Підтвердження входу та нагадування про задачі через Telegram-бота",
                "Проєктування схеми даних у PostgreSQL",
                "Розгортання й супровід на Linux-сервері: Nginx, PM2, бекапи, "
                "розбір проблем за логами",
            ],
            "challenge": "",
            "result": "",
            "code": {"text": "Закритий, тому тільки опис", "url": ""},
            "stack": CRM_STACK,
        },
        {
            "title": "SwapDesk",
            "glyph": "SWAP",
            "period": "",
            "status": {"label": "Демо", "kind": "demo"},
            "purpose": (
                "Операційний шар обмінного крипто-сервісу: котирування, життєвий цикл "
                "замовлень, кабінети клієнтів, чат підтримки й консоль оператора."
            ),
            "functions": [
                "Калькулятор обміну з живими котируваннями та розбивкою комісій",
                "Сторінка замовлення зі статусами від очікування до завершення, "
                "адресою депозиту та QR-кодом",
                "Правила ціноутворення: ручні курси для пар і активів, націнка до ринку, "
                "ліміти, імпорт і експорт у JSON",
                "Консоль оператора: замовлення, клієнти, каталог активів",
                "Чат підтримки в реальному часі на Socket.IO: вкладення, статус "
                "«прочитано», призначення оператора, експорт розмови",
                "Кабінет клієнта: профіль, історія замовлень, збережені адреси; вхід "
                "за паролем або кодом з пошти",
                "Інтерфейс EN / RU",
            ],
            "challenge": "",
            "result": (
                "Завершена демо-версія з вигаданим брендом і чистою історією Git — без "
                "даних клієнтів і конфігурації продакшену. Розрахунки в блокчейні "
                "свідомо за рамками: це питання ліцензії та провайдера ліквідності, а не коду."
            ),
            "code": {"text": "github.com/sclod/swapdesk", "url": SWAP_CODE_URL},
            "stack": SWAP_STACK,
        },
        {
            "title": "VehicleFlow Demo",
            "glyph": "VF",
            "period": "",
            "status": {"label": "Демо", "kind": "demo"},
            "purpose": "Трекінг замовлень авто.",
            "functions": [
                "Публічний сайт",
                "Кабінет клієнта з етапами доставки та маршрутом",
                "Адмінка з авторизацією",
                "Керування лідами й конвертація їх у замовлення",
            ],
            "challenge": "",
            "result": "Санітизована версія з вигаданими даними.",
            "code": {"text": "github.com/sclod/vehicleflow-demo", "url": VF_CODE_URL},
            "stack": VF_STACK,
        },
        {
            "title": "Telegram-боти для бізнесу",
            "glyph": "BOT",
            "period": "2023 — 2024",
            "status": None,
            "purpose": "",
            "functions": [
                "Бот для рієлторської компанії: інтегрував їхню базу об'єктів, зробив "
                "каталог нерухомості й розширену систему фільтрів і пошуку. По суті "
                "замінив замовнику сайт.",
                "Боти-магазини: каталог, кошик, повний сценарій замовлення — стани "
                "діалогу, обробка callback-подій, робота з БД, адмін-частина.",
            ],
            "challenge": "",
            "result": "",
            "code": None,
            "stack": BOTS_STACK,
        },
    ],
    "stack": [
        {
            "level": "Впевнено",
            "note": "",
            "items": [
                "Python",
                "aiogram / Telegram Bot API",
                "SQL, PostgreSQL",
                "REST API",
                "Linux (VPS)",
                "Nginx",
                "Git",
            ],
        },
        {
            "level": "Працював",
            "note": "",
            "items": [
                "Flask",
                "FastAPI",
                "Django",
                "SQLite",
                "PM2, systemd",
                "інтеграції зі сторонніми API",
            ],
        },
        {
            "level": "З AI-інструментами",
            "note": "пишу разом із Claude, дебажу й підтримую",
            "items": ["Next.js", "React", "TypeScript", "Prisma"],
        },
    ],
    "strengths": [
        "Швидко розбираюся в незнайомому — документація, чужий код, схожі кейси",
        "AI-assisted розробка з відповідальністю: ставлю задачу, перевіряю результат, "
        "не пускаю в прод те, чого не розумію",
        "Troubleshooting: шукаю причину збою за логами застосунку й сервера",
        "Самостійність, коли вимоги сформульовані частково",
    ],
    "about": {
        "text": (
            "Сильна сторона — не «написати з нуля по пам'яті», а розібратися: знайти "
            "причину збою за логами, зрозуміти чужий код, зв'язати кілька систем і "
            "довести до робочого стану."
        ),
        "fields": [
            {"label": "Освіта", "value": "Комп'ютерна академія ШАГ, Київ — курс Python, 2021"},
            {"label": "Англійська", "value": "Elementary, читаю технічну документацію"},
        ],
        # Журнал — лише факти з датами. Без дати запис сюди не потрапляє.
        "log": [
            {"date": "2023 — дотепер", "event": "CRM для юридичної практики, у продакшені"},
            {"date": "2023 — 2024", "event": "Telegram-боти для бізнесу"},
            {"date": "2021", "event": "Комп'ютерна академія ШАГ, Київ — курс Python"},
        ],
    },
}

EN = {
    "lang": "en",
    "locale": "en_US",
    "site": {
        "title": "Internal systems for business — CRM, Telegram bots, integrations",
        "description": (
            "Developer based in Kyiv. I build internal systems for business — CRM, "
            "Telegram bots, integrations, routine automation. Core: Python and SQL."
        ),
        "og_alt": "Internal systems for business: CRM, Telegram bots, integrations.",
    },
    "ui": {
        "skip": "Skip to content",
        "home": "Back to top",
        "brand": "portfolio",
        "nav_label": "Page sections",
        "nav": {
            "projects": "Projects",
            "stack": "Stack",
            "strengths": "Strengths",
            "about": "About",
            "contacts": "Contacts",
        },
        "lang_switch": {"label": "UA", "title": "Українська версія", "href": "../", "hreflang": "uk"},
        "kicker": "// developer · Strong Junior · Kyiv",
        "h1": ["Internal systems", "for business"],
        "cta": "Message me",
        "cta_sr": "on Telegram",
        "records": ("record", "records", "records"),
        "stack_label": "// from the foundation up",
        "strengths_label": "// how I work",
        "about_label": "// in short",
        "contacts_label": "// get in touch",
        "built": "What I built",
        "challenge": "What was hard",
        "result": "Result",
        "code": "Code",
        "code_link": "Code on GitHub",
        "log": "Log",
    },
    "hero": {
        "lead": "CRM, Telegram bots, integrations, routine automation.",
        "text": (
            "Core: Python and SQL. I build the web part with heavy use of AI tools: "
            "I set the task, review the result, debug, and take responsibility for "
            "how it runs in production."
        ),
        "code": [
            ("level", "Strong Junior"),
            ("city", "Kyiv"),
            ("core", ["Python", "SQL"]),
            ("builds", ["CRM", "Telegram bots", "integrations", "routine automation"]),
            ("contact", "@D0SIDE0"),
        ],
    },
    "projects": [
        {
            "title": "CRM for a law practice",
            "glyph": "CRM",
            "period": "2023 — present",
            "status": {"label": "In production", "kind": "prod"},
            "purpose": "Internal system, built from scratch and maintained by me.",
            "functions": [
                "Client cards, documents, tasks, contract deadline reminders",
                "ADMIN / OPERATOR / VIEWER role model with access separation",
                "User action log and change history for every card",
                "Login confirmation and task reminders via a Telegram bot",
                "PostgreSQL data schema design",
                "Deployment and maintenance on a Linux server: Nginx, PM2, backups, "
                "troubleshooting through logs",
            ],
            "challenge": "",
            "result": "",
            "code": {"text": "Closed source, so description only", "url": ""},
            "stack": CRM_STACK,
        },
        {
            "title": "SwapDesk",
            "glyph": "SWAP",
            "period": "",
            "status": {"label": "Demo", "kind": "demo"},
            "purpose": (
                "The operational layer of a crypto exchange desk: quotes, order lifecycle, "
                "customer accounts, support chat and an operator console."
            ),
            "functions": [
                "Swap calculator with live quotes and a fee breakdown",
                "Order page with statuses from waiting to completed, a deposit address "
                "and a QR code",
                "Pricing rules: manual rates for pairs and assets, markup over market, "
                "limits, JSON import and export",
                "Operator console: orders, customers, asset catalogue",
                "Real-time support chat on Socket.IO: attachments, read receipts, "
                "agent assignment, transcript export",
                "Customer account: profile, order history, saved addresses; sign-in "
                "with a password or an email code",
                "EN / RU interface",
            ],
            "challenge": "",
            "result": (
                "Completed demo with a fictional brand and a clean Git history — no "
                "customer data and no production configuration. On-chain settlement is "
                "deliberately out of scope: that's a licensing and liquidity-provider "
                "question, not a code one."
            ),
            "code": {"text": "github.com/sclod/swapdesk", "url": SWAP_CODE_URL},
            "stack": SWAP_STACK,
        },
        {
            "title": "VehicleFlow Demo",
            "glyph": "VF",
            "period": "",
            "status": {"label": "Demo", "kind": "demo"},
            "purpose": "Car order tracking.",
            "functions": [
                "Public website",
                "Client dashboard with delivery stages and route",
                "Admin panel with authentication",
                "Lead management and converting leads into orders",
            ],
            "challenge": "",
            "result": "Sanitized version with made-up data.",
            "code": {"text": "github.com/sclod/vehicleflow-demo", "url": VF_CODE_URL},
            "stack": VF_STACK,
        },
        {
            "title": "Telegram bots for business",
            "glyph": "BOT",
            "period": "2023 — 2024",
            "status": None,
            "purpose": "",
            "functions": [
                "Bot for a real estate agency: integrated their property database, built "
                "a property catalog with advanced filters and search. In effect, it "
                "replaced the client's website.",
                "Shop bots: catalog, cart, full ordering flow — dialog states, callback "
                "handling, database work, admin side.",
            ],
            "challenge": "",
            "result": "",
            "code": None,
            "stack": BOTS_STACK,
        },
    ],
    "stack": [
        {
            "level": "Confident",
            "note": "",
            "items": [
                "Python",
                "aiogram / Telegram Bot API",
                "SQL, PostgreSQL",
                "REST API",
                "Linux (VPS)",
                "Nginx",
                "Git",
            ],
        },
        {
            "level": "Have worked with",
            "note": "",
            "items": [
                "Flask",
                "FastAPI",
                "Django",
                "SQLite",
                "PM2, systemd",
                "third-party API integrations",
            ],
        },
        {
            "level": "With AI tools",
            "note": "I write it together with Claude, debug and maintain it",
            "items": ["Next.js", "React", "TypeScript", "Prisma"],
        },
    ],
    "strengths": [
        "Quick to figure out the unfamiliar — documentation, other people's code, similar cases",
        "AI-assisted development with responsibility: I set the task, review the result, "
        "and don't ship to production what I don't understand",
        "Troubleshooting: I find the cause of a failure in application and server logs",
        "Self-directed when requirements are only partly defined",
    ],
    "about": {
        "text": (
            "My strength isn't writing things from scratch from memory — it's figuring "
            "things out: finding the cause of a failure in the logs, understanding "
            "someone else's code, connecting several systems and getting it all working."
        ),
        "fields": [
            {"label": "Education", "value": "IT STEP Computer Academy, Kyiv — Python course, 2021"},
            {"label": "English", "value": "Elementary, I read technical documentation"},
        ],
        "log": [
            {"date": "2023 — present", "event": "CRM for a law practice, in production"},
            {"date": "2023 — 2024", "event": "Telegram bots for business"},
            {"date": "2021", "event": "IT STEP Computer Academy, Kyiv — Python course"},
        ],
    },
}

LANGS = [UK, EN]
