## Проект "FastAPI Application Deployment with GitHub Integration"

<p>Работа с Github, создание репозитория, внесение изменений с помощью Pull requests</p>

## Описание

Проект представляет собой комплексный набор инструкций и методологий для разработки, управления<br>
и развертывания веб-приложений с использованием FastAPI и интеграции с платформой
GitHub

## Начало работы

Эти инструкции помогут вам получить копию проекта и запустить его на вашем локальном компьютере.

### Предварительные требования

Что вам потребуется установить, прежде чем начать работу с проектом:

- Зарегистрироваться на Github
- Создать репозиторий и ветку dev внутри
- Написать приложение на FastApi

[Для загрузки сразу всех библиотек](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

Загрузить библиотеки -->

```
fastapi==0.103.1
uvicorn==0.23.2
```

### Добавить проект в репозиторий

Команды:

```
git status - проверить файлы
git add . - добавить новые файлы
git commit -m "commit"  - закоммитеть файлы
git pull - применить изменения если они были на github
git push - загрузить на git
```

### Внесение изменений с помощью Pull requests

Команды:

```
git branch feature/my_name - создание ветки 
git checkout feature/my_name - переход на ветку
```

### Развернуть проект в Docker

- Скачать и установить Docker
- Создать Dockerfile в вашем проекте

Команды:

```
docker build -t my_image . - создание образа
docker run -d --name my_container -p 8000:8000 my_image - запуск контейнера
```

### Разворот базы данных в контейнере и связь с приложением

- Создать файл docker-compose.yml в проекте

Команды:

```
docker-compose up -d --build - Соберет образы со всеми зависимостями и запустит
docker image prune - удаление образов none
```

### Привязка приложения к базе данных и произведение миграции

Загрузить библиотеки -->

```
- SQLAlchemy==2.0.21
- psycopg2-binary==2.9.7
- alembic==1.12.0
- pydantic==2.3.0
```

Команды:

```
alembic init alembic - создать папку alembic
alembic revision --autogenerate -m "Testing table" - создание миграции
alembic upgrade head  - применение миграции к базе 
```

### Парсинг Excel файлов (pandas, openpyxl )

- Создать файл excel_parser.py в проекте

Загрузить библиотеки -->

```
-python-multipart==0.0.6
-pandas==2.1.1
-openpyxl==3.1.2
```