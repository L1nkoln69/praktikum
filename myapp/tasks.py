from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def contact_us(email, remind):
    send_mail('REMINDER',
              f'{remind}',
              'orlov229003@gmail.com',
              [email],
              fail_silently=False
              )
