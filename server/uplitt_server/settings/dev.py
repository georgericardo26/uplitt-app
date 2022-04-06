import os

from .base import *


DEBUG = True

ALLOWED_HOSTS = ["*"]
SERVER_NAME = "18.118.105.254"
SERVER_PORT = "80"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT")
    }
}
