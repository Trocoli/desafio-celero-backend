from __future__ import absolute_import, unicode_literals

import os 

from celery import Celery

from celery_proj import celery_proj 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_proj.settings')


app = Celery('celery_proj')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
