# Django сервис друзей
## Стек:
- **Django + Django REST framework**
- **PostgresSQL** - база данных
- **SwaggerUI** - OpenApi документирование

## Как запустить:
 1. `git clone https://github.com/NeOleksiy/friends_service.git`
 2. Через psql в терминале или через pgadmin создаём базу данных 
 3. В friend_service/settings.py в cписке `DATABASE = []` вводим свои данные
 4. В терминале `python3 -m venv env`
 5. В терминале `venv/bin/activate`
 6. В терминале `pip install -r requirements.txt`
 7. В терминале `./python3 manage.py migrate`
 8. В терминале `./python3 manage.py runserver`
 - Для запуска тестов `./python3 manage.py test`
 
## Как работает:
### Для доступа к документации OpenApi переходим по http://127.0.0.1:8000/swagger/
![OpenApi документация](/screenshots/swagger.png)
### Например для регистрации пользователя отправляем Post запрос на http://127.0.0.1:8000/register/
![Регистрация](/screenshots/register.png)
### Для отправки запроса в друзья отправляем Patch запрос на http://127.0.0.1:8000/invite_or_delete/<id1>/<id2>/
Где id1 - id пользователя отправляющего запрос, а id2 - id пользователя принимающего запрос
![инвайт](/screenshots/invite.png)
### Для удаления из друзей отправляем Delete запрос на http://127.0.0.1:8000/invite_or_delete/<id1>/<id2>/
Где id1 - id пользователя удаляющего из друзей, а id2 - id пользователя кого удалили из друзей
![инвайт](/screenshots/remove.png)

  
