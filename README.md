# MongoDB Quotes Scraper

Навчальний проєкт з NoSQL: CRUD-операції в MongoDB на прикладі колекції котів та парсинг сайту [quotes.toscrape.com](https://quotes.toscrape.com/) із завантаженням цитат і авторів у базу.

## Що робить проєкт

### Частина 1. CRUD у MongoDB (`task1_mongodb.py`)

Робота з колекцією `cats` у базі `pet_info`. Кожен документ має поля `name`, `age`, `features`.

| Функція | Дія |
|---|---|
| `add_info_to_collection` | додає 9 котів у колекцію |
| `get_all_record_from_collection` | виводить усі документи |
| `get_info_by_name` | знаходить кота за ім'ям |
| `update_age_by_name` | змінює вік |
| `update_features_by_name` | додає нові характеристики (`$push` + `$each`) |
| `delete_record_by_name` | видаляє документ за ім'ям |
| `delete_all_record` | очищує колекцію |

### Частина 2. Парсинг і завантаження в базу

| Файл | Призначення |
|---|---|
| `task2_parsing.py` | проходить усі сторінки сайту, збирає цитати (текст, автор, теги) і сторінки авторів (ім'я, дата та місце народження, опис), зберігає їх у `quote.json` і `authors.json` |
| `task2_add_to_db.py` | завантажує обидва файли в базу `famous_quote`, колекції `quote` і `authors` |
| `quote.json` | 100 цитат |
| `authors.json` | 50 авторів |

## Запуск

Потрібні Python 3.13 і [Poetry](https://python-poetry.org/).

1. Клонуй репозиторій і встанови залежності:

   ```bash
   git clone https://github.com/SHEV-4/mongodb-quotes-scraper.git
   cd mongodb-quotes-scraper
   poetry install
   cd src/goit_ds_hw_03
   ```

2. Створи безкоштовний кластер у [MongoDB Atlas](https://www.mongodb.com/atlas) і скопіюй рядок підключення.

3. Передай рядок підключення через змінну середовища `MONGODB_URI`:

   ```bash
   export MONGODB_URI="mongodb+srv://<користувач>:<пароль>@<кластер>.mongodb.net/?retryWrites=true&w=majority"
   ```

   У Windows PowerShell: `$env:MONGODB_URI = "..."`.

4. Запусти потрібний скрипт (з папки `src/goit_ds_hw_03`):

   ```bash
   python task1_mongodb.py        # приклад операції з колекцією cats
   python task2_parsing.py        # зібрати цитати й авторів у JSON-файли
   python task2_add_to_db.py      # завантажити JSON-файли в MongoDB
   ```

> **Безпека.** Ніколи не зберігай логін і пароль до бази в коді чи в репозиторії. Використовуй змінні середовища.

## Структура проєкту

```
.
├── src/goit_ds_hw_03/
│   ├── task1_mongodb.py
│   ├── task2_parsing.py
│   ├── task2_add_to_db.py
│   ├── quote.json
│   └── authors.json
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Що використано

Python, MongoDB Atlas, PyMongo, Requests, Beautiful Soup, Poetry.
