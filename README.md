# FastAPI тестовое задание на собеседование в ООО «ПАТРЕС»
Инструкция по запуску
1. Запуск контейнера с базой данных
```
  docker-compose up
```
2. Создание вертуальной среды
```
  python -m venv .venv
```
3. Запуск вертуальной среды
```
  .venv/Scripts/activate
```
4. Установка библиотек
```
  pip install --no-cache-dir -r requirements.txt
```
5. Запуск миграций
```
  alembic upgrade head
```
6. Запуск сервера
```
  uvicorn app.main:app --host 0.0.0.0 --port 8000
```
7. Переход на запущенный <a href="http://localhost:8000/docs">сервер</a>
