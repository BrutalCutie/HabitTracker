# Описание проекта
Проект даёт возможность управлять полезными привычками. Отправка уведомлений,
чтобы не забыть о привычках происходит через telegram бота.
<br>
При разработке использовалась БД sqlite3
<hr>

# <a href='https://github.com/BrutalCutie/HabitTracker/blob/8d1fbfb4d3cbd7ddebbbb5424178a85cb558a895/.github/workflows/Ci-CdGuide.md'>Гайд для CI/CD на Docker-compose</a>
### <a href='http://77.232.138.209/'>Работающее приложение</a>
<br>
<hr>

# Установка
Проект был написан через poetry.

- **Клонируйте репозиторий**<br>
```git clone https://github.com/BrutalCutie/HabitTracker.git```<br><br>

- **Установите зависимости**<br>
С помощью poetry или другим удобным для вас способом. В проекте имеется 
как .toml, так и requirements.txt<br><br>
 
- **Чувствительные данные**<br>
Для работы вам потребуется некоторые данные для функционирования программы.<br>
Все необходимые для заполнения данные содержатся в файле .env_sample.<br>
Переименуйте его в .env и подставьте ваши данные. У вас не должно возникнуть сложностей, 
они подробно описаны.<br><br>

- **Примените миграции**<br>
```python manage.py migrate```<br><br>

- **Запуск сервера**<br>
```python manage.py runserver```<br><br>

<hr>

# Endpoints

- **Регистрация пользователя**<br>
POST /users/<br>
{**"username"**: ...,
**"email"**: ...,
**"telegram_id"**,
**"password"**: ...}<br><br>

- **Получение токена авторизации**<br>
POST /users/token/<br>
{
    **"username"**: ...,
    **"password"**: ...
}<br><br>


- **Регистрация полезной привычки**<br>
POST /habits/<br>
{
    **"action"**: ...,
    **"publish_to_all"**: ...,
    **"reward"**: ...,
    **"time"**: ...,
    **"time_to_complete"**: ...,
    **"is_nice_habit"**: ...,
    **"place"**: ...
}<br><br>

- **Регистрация приятной привычки**<br>
POST /habits/<br>
{
    **"action"**: ...,
    **"publish_to_all"**: ...,
    **"is_nice_habit"**: ...
}<br><br>

- **Получение списка своих привычек**<br>
GET /habits/<br>
<br>

- **Получение списка опубликованных привычек**<br>
GET /published-habits/<br>
<br>

- **Просмотр опубликованной привычки**<br>
GET /published-habits/\<int:pk>/<br>
<br>

Свои привычки можно так-же изменять и удалять

<hr>

# Celery
### В проекте присутствует периодическая задача, по уведомлению пользователей привычек, что им пока выполнять те самые привычки

### Для корректной работы необходимо запустить REDIS сервер
Для установки на Windows воспользуйтесь WSL или инструкцией: https://github.com/MicrosoftArchive/redis/releases
### Запуск Celery Worker ```celery -A config worker -l INFO```
Обратите внимание, что для Windows при указании обработчика событий необходимо добавить флаг 
**-P eventlet**
### Запуск Celery Beat ```celery -A config beat -l INFO```


<hr>

# Полезное
- <a href="https://t.me/BotFather">Папа ботов<a>
- <a href="https://t.me/my_id_bot">Узнать свой TelegramID<a>
