"""
WSGI config for uplitt_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


settings_file = os.getenv('SETTINGS_ENV')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_file)


application = get_wsgi_application()
