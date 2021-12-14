from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

"""
    Celery App을 생성하는 파일 
"""
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings.base')

app = Celery('worker', include=['celerytest.views'])

app.config_from_object('base.settings.celeryconfig', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
