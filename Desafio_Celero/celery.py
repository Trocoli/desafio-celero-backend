import os

from celery import Celery 

from django.conf import settings 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'desafio_celero.settings')
app = Celery('desafio_celero.celery')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)