<h1 align="center">Welcome to Django Boilerplate with Simple Security Config. 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/neustren" target="_blank">
    <img alt="Twitter: neustren" src="https://img.shields.io/twitter/follow/neustren.svg?style=social" />
  </a>
</p>

> Django boilerplate with security configured and env keys hidden. Good for your django/python learning courses.
> Comes with admin_honeypot, bootstrap4 and configurations for Portuguese-BR template.

## Install

```sh
git clone https://github.com/Neustren/django-boilerplate
python -m venv venv
source venv/bin/activate # GNU/Linux
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
cp example.env .env # copy example.env to .env file
```

## Usage

```sh
python manage.py runserver # For dev
python manage.py runserver --settings=backend.settings.prod # For production envs
```

## Languages and libs used :books:

- [Python3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Admin Honeypot](https://pypi.org/project/django-admin-honeypot/)
- [Bootstrap4](https://pypi.org/project/django-bootstrap4/)
- [Postgresql](https://pypi.org/project/psycopg2/)
- [Decouple](https://pypi.org/project/python-decouple/)


## Author

👤 **William Franco**

* Website: http://neustren.org
* Twitter: [@neustren](https://twitter.com/neustren)
* Github: [@neustren](https://github.com/neustren)

## Show your support

Give a ⭐️ if this project helped you!

<a href="https://www.patreon.com/neustren">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_