В этом небольшом проекте я попытался применить опыт работы с гексагональной архитектурой и фреймворк FastApi. Получилось не без небольших костылей, таких как файл api_project/aplication/app.py, нарушающий логику единой точки инициализации приложения. Однако остановился на этом варианте, так как на мой взгляд, другие подходы (например отсюда: https://github.com/fastapi/fastapi/discussions/8991) либо выглядят не лучше, либо нарушают исходный синтаксис фреймворка. 

Для тестового запуска необходимо:

1. Создать и заполнить файл с переменными окружения:

```
DATABASE_HOST=postgres
DATABASE_NAME=my_db
DATABASE_PASS=root
DATABASE_PORT=5432
DATABASE_USER=root

RABBIT_BASE_QUEUE=base_queue
RABBIT_USER=root
RABBIT_PASS=root
RABBIT_HOST=rabbitmq
```

2. Запустить проект командой

```
docker-compose up -d --build
```

3. Работа с API

Документация будет доступна по "http://localhost:8004/docs"

Примеры запросов:

Запрос для создания новой задачи. 
- POST: http://localhost:8004/tasks/
```
{
  "name": "string"
}
```

Запрос вывода существующих задач с возможностью вильтрации по статусу.
- GET: http://localhost:8004/tasks/?status=failed

Получение информации об одной конкретной задаче.
- http://localhost:8004/tasks/1
