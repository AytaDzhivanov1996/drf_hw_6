import hashlib

import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from skypro.models import Subscription, PaymentLog


@shared_task
def check_course_update(course_pk):
    subscription_data = Subscription.objects.filter(course_id=course_pk)
    for item in subscription_data:
        send_mail(
            subject='Подписка на курс',
            message='Курс был обновлен, проверьте изменения',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[item.owner.email],
            fail_silently=False
        )
        print(f'Письмо было отправлено {item.owner.email}')


@shared_task
def check_status():
    checked_data = PaymentLog.objects.filter(Status='NEW')
    if checked_data.exists():
        for item in checked_data:
            token_str = str(settings.TERMINAL_PASSWORD) + str(item.PaymentID) + str(settings.TERMINAL_KEY)
            hashed_token = hashlib.sha256(token_str.encode())
            token = hashed_token.hexdigest()

            data_for_request = {
                "TerminalKey": settings.TERMINAL_KEY,
                "PaymentID": item.PaymentID,
                "Token": token
            }
            response = requests.post('https://securepay.tinkoff.ru/v2/GetState', json=data_for_request)
            item.Status = response.json().get("Status")
            item.save()
