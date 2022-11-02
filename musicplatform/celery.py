from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')

app = Celery('musicplatform')

app.config_from_object(settings, namespace='CELERY_CONF')

app.autodiscover_tasks()


# Celery Beat Settings

app.conf.beat_schedule = {

}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
