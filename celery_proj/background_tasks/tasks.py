from __future__ import absolute_import, unicodde_literals

from celery import shared_task

@shared_task
def add(x,y):
    return x + y