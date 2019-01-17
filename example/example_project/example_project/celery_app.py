# coding: utf-8
from __future__ import absolute_import
import os
from celery import Celery as CoreCelery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example_project.settings')


class Celery(CoreCelery):
    pass

app = Celery('example_project')
app.config_from_object('example_project.settings_celery')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
