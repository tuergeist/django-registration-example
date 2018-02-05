# django-registration-example
How to use and customize django-registration to have a self-service signup form for users including email-activation

## Purpose

I was looking for a working minimal example how I can conduct user signup for a django app. 
Requirements were:
- Write least code possible
- Have Email verification/activation
- Could be customized to have `email` as `username`

## Uses

- Python 3
- Django 2.0
- django-registration development https://github.com/ubernostrum/django-registration (note: releases before v3 do not work with Django 2)

## How to

Let's assume we're in `~/git` and you might be inside a virtualenv

- `git clone https://github.com/ubernostrum/django-registration`
- `cd django-registration`
- `pip install -e`
- `cd ..`
- `git clone https://github.com/tuergeist/django-registration-example.git`
- `cd django-registration-example`
``` 
git clone https://github.com/ubernostrum/django-registration
cd django-registration
pip install -e
cd ..
git clone https://github.com/tuergeist/django-registration-example.git
cd django-registration-example
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8888
```
Visit http://127.0.0.1:8888/accounts/register/ to register a new user.

## How it looks like

![Registration Page](https://raw.githubusercontent.com/tuergeist/django-registration-example/master/docs/register-tac.png)
