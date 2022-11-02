from celery import shared_task
from django.core.mail import send_mail
from musicplatform import settings
from artists.models import Artist

@shared_task(bind=True)
def send_mail_task(self, album_name, artist_id):
    artist = Artist.objects.get(id=artist_id)
    send_mail(
        subject = "Congratulations",
        message= f"Congratulations {artist.stage_name} on your new album {album_name}",
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=[artist.user.email,],
        fail_silently= False,
    )

    return "Sent"
