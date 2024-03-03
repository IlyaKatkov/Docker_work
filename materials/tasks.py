from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from celery import shared_task
from subscription.models import Subscription


@shared_task
def send_email_update_course(course):
    subscriptions = Subscription.objects.all().filter(course=course)
    users = []
    for subscription in subscriptions:
        users.append(subscription.user)
    for user in users:
        message = f"Привет {user.name}. {course.name} был обновлён."
        send_mail(
            subject="Обновление курса",
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )