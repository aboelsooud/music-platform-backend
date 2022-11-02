from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')

app = Celery('musicplatform')
app.conf.enable_utc = False

app.conf.update(timezone = 'Africa/Cairo')

app.config_from_object(settings, namespace='CELERY_CONF')

app.autodiscover_tasks()


# Celery Beat Settings

app.conf.beat_schedule = {
    'send-email-every-day-at-midnight': {
        'task' : 'albums.tasks.send_mail_every_day_task',
        'schedule' : crontab(hour=0, minute=0),
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
