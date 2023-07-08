# QRKot Spreadsheets

[![Python](https://img.shields.io/badge/-Python3-464646?style=flat&logo=Python&logoColor=ffffff&color=informational)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=informational)](https://flask.palletsprojects.com/en/2.3.x/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=informational)](https://www.sqlalchemy.org/)

## Описание

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

![Result](https://github.com/whodef/QRkot_spreadsheets/assets/7266512/3293428a-cd81-4d40-9401-45418e4a695a)

## Запуск проекта

1. Клонируйте репозиторий и перейдите в него
    ```bash
   https://github.com/whodef/QRkot_spreadsheets.git
   ```
2. Установите и активируйте виртуальное окружение
    ```bash
   python3 -m venv venv
   ```
   
   * Если у вас Linux/MacOS: `source venv/bin/activate`
   
   * Если у вас Windows: `source venv/scripts/activate`


3. Установите зависимости из файла requirements.txt
    ```bash
    python3 -m pip install --upgrade pip
    ```
    ```bash
    pip3 install -r requirements.txt
    ```
   
4. Создайте файл .env и заполните его своими значениями

   ```bash
   cp .env.example .env
   ```
   
5. Примените миграции
   ```angular2html
   alembic upgrade head
   ```
   
6. Запустите проект
   ```bash
   uvicorn app.main:app --reload
   ```

## Автор проекта

**[Tatiana Seliuk](https://github.com/whodef)**
