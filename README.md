Medical Information System (MIS)<br>
Описание проекта<br>
Данный проект представляет собой учебное веб-приложение в стиле медицинской информационной системы (МИС).<br>
Система предназначена для регистрации пользователей (врачей), аутентификации, а также поиска пациентов.<br>
Проект реализован с использованием Django, Django REST Framework и JWT-аутентификации.<br>
Frontend выполнен на HTML, CSS и JavaScript без использования сторонних фреймворков.<br>

Используемый стек технологий
Backend<br>
    • Python<br>
    • Django<br>
    • Django REST Framework<br>
    • Simple JWT<br>
    • SQLite (может быть заменена на PostgreSQL)<br>
Frontend<br>
    • HTML5<br>
    • CSS3<br>
    • JavaScript (Fetch API)<br>
<br>
Функциональные возможности<br>
Аутентификация и авторизация<br>
    • Регистрация нового пользователя<br>
    • Авторизация по логину и паролю<br>
    • JWT access и refresh токены<br>
    • Сохранение сессии на клиенте<br>
    • Выход из системы<br>
Работа с пациентами<br>
    • Поиск пациентов по имени или фамилии<br>
    • Доступ к поиску только для авторизованных пользователей<br>
Роли пользователей<br>
    • Гость (неавторизованный пользователь)<br>
    • Авторизованный пользователь (врач)<br>
    • Администратор (Django superuser)<br>

Архитектура проекта<br>
Проект построен в соответствии с принципами:<br>
    • REST<br>
    • DRY<br>
    • Разделение ответственности (users, patients)<br>
    • Использование высокоуровневых представлений DRF<br>
    • Серверная и клиентская валидация данных<br>

Структура проекта<br>
MIS/<br>
├── clinic/ # основное приложение (модели, API, сериалайзеры)<br>
├── MIS/<br>
│   ├── settings.py<br>
│   ├── urls.py<br>
│   ├── wsgi.py<br>
│   └── asgi.py<br>
├── frontend/<br>
│   ├── index.html<br>
│   ├── login.html<br>
│   ├── register.html<br>
│   ├── search.html<br>
│   ├── styles.css<br>
│   ├── login.js<br>
│   ├── register.js<br>
│   └── search.js<br>
├── db.sqlite3<br>
├── manage.py<br>

Установка и запуск проекта
1. Клонировать проект
git clone <repository_url>
cd MIS
2. Создать виртуальное окружение<br>
python -m venv venv<br>
source venv/bin/activate<br>
3. Установить зависимости
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary
4. Применить миграции
python manage.py makemigrations
python manage.py migrate
5. Создать администратора
python manage.py createsuperuser
6. Запустить сервер
python manage.py runserver 127.0.0.1:<9932 – или любой другой не занятый порт>
