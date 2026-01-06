Medical Information System (MIS)
Описание проекта
Данный проект представляет собой учебное веб-приложение в стиле медицинской информационной системы (МИС).
Система предназначена для регистрации пользователей (врачей), аутентификации, а также поиска пациентов.
Проект реализован с использованием Django, Django REST Framework и JWT-аутентификации.
Frontend выполнен на HTML, CSS и JavaScript без использования сторонних фреймворков.

Используемый стек технологий
Backend
    • Python
    • Django
    • Django REST Framework
    • Simple JWT
    • SQLite (может быть заменена на PostgreSQL)
Frontend
    • HTML5
    • CSS3
    • JavaScript (Fetch API)

Функциональные возможности
Аутентификация и авторизация
    • Регистрация нового пользователя
    • Авторизация по логину и паролю
    • JWT access и refresh токены
    • Сохранение сессии на клиенте
    • Выход из системы
Работа с пациентами
    • Поиск пациентов по имени или фамилии
    • Доступ к поиску только для авторизованных пользователей
Роли пользователей
    • Гость (неавторизованный пользователь)
    • Авторизованный пользователь (врач)
    • Администратор (Django superuser)

Архитектура проекта
Проект построен в соответствии с принципами:
    • REST
    • DRY
    • Разделение ответственности (users, patients)
    • Использование высокоуровневых представлений DRF
    • Серверная и клиентская валидация данных

Структура проекта
MIS/
├── clinic/ # основное приложение (модели, API, сериалайзеры)
├── MIS/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── search.html
│   ├── styles.css
│   ├── login.js
│   ├── register.js
│   └── search.js
├── db.sqlite3
├── manage.py

Установка и запуск проекта
1. Клонировать проект
git clone <repository_url>
cd MIS
2. Войти в виртуальное окружение
venv\Scripts\activate
3. Установить зависимости
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary
4. Применить миграции
python manage.py makemigrations
python manage.py migrate
5. Создать администратора
python manage.py createsuperuser
6. Запустить сервер
python manage.py runserver 127.0.0.1:<9932 – или любой другой не занятый порт>
