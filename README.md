## Возможности:

- Получение, создание, обновление, удаление публикаций.
- Получение, создание, обновление, удаление комментариев к публикациям.
- Просмотр сообществ и детальной информации о них.
- Отслеживание подписок на авторов, а так же возможность подписки на интересующего автора.
- Получение, обновление и проверка JWT авторизации.

## Установка и запуск проекта в dev-режиме:
1. [ ] Склонируйте репозиторий:

```bash
git clone git@github.com:qqyall/api_final_yatube.git && cd api_yatube
```

2. [ ] Создайте и активируйте виртуальное окружение:

###### Windows:
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
```bash
python -m pip install --upgrade pip
```
###### Linux:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
python3 -m pip install --upgrade pip
```

3. [ ] Установите зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
``` 

4. [ ] Перейдите в папку с manage.py

```bash
cd api_yatube
``` 

5. [ ] Создайте миграции
###### Windows:
```bash
python manage.py makemigrations
```
###### Linux:
```bash
python3 manage.py makemigrations
```

6. [ ] Примените миграции
###### Windows:
```bash
python manage.py migrate
```
###### Linux:
```bash
python3 manage.py migrate
```

7. [ ] Запустите проект
###### Windows:
```bash
python manage.py runserver
```
###### Linux:
```bash
python3 manage.py runserver
```

После запуска проекта, документация будет доступна по адресу:
```
http://localhost:port/redoc/
```

## Примеры запросов:

### POST-запрос на добавление новой публикации (требуется токен аутентификации)

`POST http://localhost:port/api/v1/posts/`

```
{
  "text": "Text",
  "group": 1
}
```

#### Ответ:

```
{
    "id": 1,
    "author": "admin",
    "text": "Text",
    "pub_date": "2024-04-17T19:15:17Z",
    "image": null,
    "group": 1
}
```

### GET-запрос, получение информации о сообществе c id=1

`GET http://localhost:port/api/v1/groups/1/`

#### Ответ:

```
{
    "id": 1,
    "title": "first group",
    "slug": "first-group",
    "description": "group description"
}
```


## Стек
- Python 3.9
- Django 2.2
- Django REST Framework
- SQLite3
- Simple-JWT


## Об авторе
Румянцев Савелий - https://github.com/qqyall
E-mail: radogask9rsd@gmail.com  
Telegram: @clrblndd  
Россия, г. Уфа
