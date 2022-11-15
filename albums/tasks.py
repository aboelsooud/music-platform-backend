from datetime import datetime, timezone

from artists.models import Artist
from celery import shared_task
from django.core.mail import send_mail
from musicplatform import settings


@shared_task(bind=True)
def send_mail_task(self, album_name, artist_id):
    artist = Artist.objects.get(id=artist_id)
    send_mail(
        subject = "Congratulations",
        message= f"Congratulations {artist.stage_name} on your new album {album_name}.",
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=[artist.user.email,],
        fail_silently= False,
    )

    return "Sent"

@shared_task(bind=True)
def send_mail_every_day_task(self):
    for artist in Artist.objects.all():
        send = False
        if artist.album_set.all().count() == 0 :
            send = True
        else:
            album = artist.album_set.all().latest('created')
            days = datetime.now(timezone.utc) - album.created
            if days.days > 30:
                send = True
            
        if send:
            send_mail(
            subject = "Warning",
            message= "You haven't created an album in the past 30 days.\nSo, we want to let you know that your inactivity is causing your popularity on our platform to decrease.",
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[artist.user.email,],
            fail_silently= False,
            )

    return "Done"
