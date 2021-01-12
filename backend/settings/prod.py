from .base import *

from decouple import config

SECRET_KEY = config('PROD_SECRET_KEY')
DEBUG = config('PROD_DEBUG', cast=bool)

ALLOWED_HOSTS = config('PROD_ALLOWED_HOSTS', cast=lambda v: [
                       s.strip() for s in v.split(',')])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('PROD_DB_NAME'),
        'USER': config('PROD_DB_USER'),
        'PASSWORD': config('PROD_DB_PASSWORD'),
        'HOST': config('PROD_DB_HOST'),
        'PORT': '5432'
    }
}

AXES_ENABLED = True
