# djangoBillingProject
Проект "djangoBillingProject" имеет три endpoint'а:
1. Создание счета. Входные парамеры: название, флаг овердрафности (true – значит возможен нелимитированный уход в минус). Результат: идентификатор счета.

`http://127.0.0.1:8000/billing/transaction/create/`

2. Перевод денег со счета А на счет Б. Входные параметры: идентификатор счета донора, идентификатор счета реципиента, сумма перевода. Результат: успех или нет.

`http://127.0.0.1:8000/billing/transaction/create/`

3. Запрос баланса счета. Входные параметры: идентификатор счета. Результат: сумма.

`http://127.0.0.1:8000/billing/bank-account/balance/<int:pk>/`

---

# ЗАПУСК ПРОЕКТА
Запустить данный проект можно двумя способами: либо через "Dockerfile", либо через "manage.py"

---

## ЗАПУСК ПРОЕКТА ЧЕРЕЗ "Dockerfile"

Запустите Docker на Вашем компьютере и введите последовательно все нижеперечисленные команды:

`python3 manage.py migrate`

`pip install -r requirements.txt`

`docker build -t django-billing-project-f Dockerfile .`

`gunicorn djangoBillingProject.wsgi:application —bind localhost:8000`

Проект запущен.

---

## ЗАПУСК ПРОЕКТА ЧЕРЕЗ "manage.py"

Введите последовательно все нижеперечисленные команды:

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python3 manage.py migrate`

`python3 manage.py runserver`

Проект запущен.

---

## ЗАПУСК ТЕСТОВ

Введите нижепредставленную команду:

`python3 manage.py test --verbosity 1`

Тесты запущены.

---

## СОЗДАНИЕ СУПЕРЮЗЕРА ДЛЯ ДОСТУПА К АДМИНИСТРАТИВНОЙ ПАНЕЛИ DJANGO

После ввода нижепредставленной команды нужно вести логин и пароль дважды (почту вводить необязательно):

`python3 manage.py createsuperuser`

Админка доступна по url: http://127.0.0.1:8000/admin/
