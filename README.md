<!-- О проекте -->
## О проекте

Данный проект является дополнением к веб-приложению Yatube. API-интерфейс позволяет обращаться к различным эндпоинтам, перечень которых можно найти в ReDoc-документации.


<!-- Начало работы -->
## Начало работы с проектом

_Для того, чтобы запустить этот проект локально, необходимо выполнить следующие шаги:_ 

1. Склонируйте [репозиторий](https://github.com/kabachok-prog/api_final_yatube)
2. Установите виртуальное окружение:
    ```sh
   python -m venv venv
   ```
2. Установите все необходимые зависимости:
   ```sh
   pip install -r requirements.txt
   ```
3. Выполните миграции:
   ```sh
   python manage.py migrate
   ```
4. Запустите сервер:
   ```sh
   python manage.py runserver
   ```
5. Примеры запросов к API:
   ```
    1) POST-запрос на добавление нового поста:
   ```
   ```json
   {
   "text": "string",
   "image": "string",
   "group": 0
   }
   ```
   ```
   2) GET-запрос на получение комментария:
   ```
   ```sh
   'http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/'
   ```
   ```
   3) POST-запрос на подписку:
   ```
   ```sh
      {
   "following": "string"
   }
   ```
