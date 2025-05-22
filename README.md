# 🌟 Сайт "Добрые дела"

Проект создан для университетского модуля по предмету **"Технология программирования"**.

Позволяет пользователю сохранять и просматривать свои добрые дела: добавить, редактировать, удалить.  
Поддерживает авторизацию, формы и поиск.

---

## ⚙️ Функционал

- Регистрация / Авторизация
- Добавление добрых дел
- Просмотр всех дел
- Редактирование / удаление
- Поиск по названию
- Django Admin
- HTML-шаблоны и простая вёрстка

---

## 🛠 Используемое

- Python 3
- Django 4
- SQLite
- HTML / CSS

---

## 🚀 Как запустить

```bash
git clone https://github.com/yourusername/gooddeeds_project.git
cd gooddeeds_project
python3 -m venv venv
source venv/bin/activate
pip install django
python manage.py migrate
python manage.py createsuperuser  # создать админа
python manage.py runserver
