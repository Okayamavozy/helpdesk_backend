# HelpDesk backend API

	Backend построен на многослойной архитектуре
	Язык разработки - python 3.14.3
	База данных - sqlite3

# Структура проекта

```
backend  
 ┣ config  
 ┃ ┣ database.py  
 ┃ ┗ schema_config.py  
 ┣ dependencies  
 ┃ ┗ deps.py  
 ┣ interfaces  
 ┃ ┣ tasks.py  
 ┃ ┗ users.py  
 ┣ middlewares  
 ┃ ┗ middleware.py  
 ┣ models  
 ┃ ┣ tasks.py  
 ┃ ┗ users.py  
 ┣ repositories  
 ┃ ┣ tasks.py  
 ┃ ┗ users.py  
 ┣ routers  
 ┃ ┣ tasks.py  
 ┃ ┗ users.py  
 ┣ schemas  
 ┃ ┣ tasks.py  
 ┃ ┗ users.py  
 ┣ services  
 ┃ ┣ tasks.py  
 ┃ ┗ users.py  
 ┣ validations  
 ┃ ┗ errors.py  
 ┣ __init__.py
 ┗ main.py
 
```
# Библиотеки

- annotated-doc==0.0.5
- annotated-types==0.8.0
- anyio==4.16.0
- click==8.5.0
- fastapi==0.162.0
- h11==0.16.0
- idna==3.20
- opentelemetry-api==1.45.2
- pydantic==2.14.2
- pydantic_core==2.50.2
- SQLAlchemy==2.1.6
- starlette==1.10.0
- typing-inspection==0.4.4
- typing_extensions==4.16.0
- uvicorn==0.54.0

# Установка библиотек

- MacOS
```zsh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Widnows
```cmd
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

# Запуск backend

- MacOS
```zsh
python3 main.py
```

- Windows
```cmd
python main.py
```

# Эндпоинты

### Users

| Метод  | Роут             | Описание                                    |
| ------ | ---------------- | ------------------------------------------- |
| GET    | /users           | Получить список всех пользователей из БД    |
| POST   | /users           | Создать нового пользователя                 |
| GET    | /users/{user_id} | Получить конкретного пользователя по его ID |
| DELETE | /users/{user_id} | Удалить пользователя из БД по его ID        |

### Tasks

| Метод  | Роут                           | Описание                                        |
| ------ | ------------------------------ | ----------------------------------------------- |
| GET    | /tasks                         | Получить список всех задач из БД                |
| POST   | /tasks                         | Создать новую задачу                            |
| GET    | /tasks/statuses                | Получить список всех возможных статусов задачи  |
| PATCH  | /tasks/{task_id}/change-status | Изменить статус задачи по ее ID                 |
| GET    | /tasks/categories              | Получить список всех возможных категорий задачи |
| GET    | /tasks/{task_id}               | Получить конкретную задачу по ее ID             |
| DELETE | /tasks/{task_id}               | Удалить задачу из бд по ее ID                   |
