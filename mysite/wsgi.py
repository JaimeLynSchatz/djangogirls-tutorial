"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# from http://stackoverflow.com/questions/31082884/why-is-whitenoise-crashing-in-a-default-django-project-on-heroku
# application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(get_wsgi_application())