# Учебный проект API для Yatube

## Описание

API для социальной сети,  в которой можно размещать публикации с фото, комментировать записи и подписываться на других пользователей.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone http://github.com/xfatcorex/api_final_yatube_main.git

cd api_final_yatube_main
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

## Примеры запросов

### Получение JWT-токена

Необходимо отправить POST-запрос на адрес `http://127.0.0.1:8000/api/v1/jwt/create/`
и передать обязательные поля `username` и `password`.

Пример запроса:
```
{
    "username": username,
    "password": password
}
```
Пример ответа:
```
{
    "refresh": token,
    "access": token
}
```
### Получение списка публикаций

Необходимо отправить POST-запрос на адрес `http://127.0.0.1:8000/api/v1/posts/` 
и передать обязательное поле `text`, так же можно передать необязательные поля `image` и `group`

Пример запроса:
```
{
    "text": "Моя первая публикация",
    "image": "data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAoAAAAGqCAYAAACbEvXuAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAACgKADAAQAAAABAAABqgAAAAD+"
    "group": 1
}
```
Пример ответа:
```
{
    "id": 0,
    "author": "Anton",
    "text": "Моя первая публикация",
    "pub_date": "2024-06-14T14:15:22Z",
    "image": "http://127.0.0.1:8000/media/posts/images/temp.png",
    "group": 1
}
```
### Подписка на пользователя

Необходимо отправить POST-запрос на адрес `http://127.0.0.1:8000/api/v1/follow/` 
и передать обязательное поле `following`

Пример запроса:
```
{
    "following": "Petr"
}
```
Пример ответа:
```
{
    "user": "Anton",
    "following": "Petr"
}

Более подробную информацию о запросах можно получить по адресу `http://127.0.0.1:8000/redoc/`
