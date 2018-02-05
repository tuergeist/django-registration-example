# django-registration-example
How to use and customize django-registration to have a self-service signup form for users including email-activation

Uses:
- Python3
- Django2
- django-registration development https://github.com/ubernostrum/django-registration

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
