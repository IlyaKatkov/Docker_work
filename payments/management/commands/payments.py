from django.core.management import BaseCommand
from payments.models import Payment


test_payments = [
    {
        "user_id": 1,
        "date": "2024-02-01",
        "course_id": 1,
        "amount": 10000,
        "method": "T",
    },
    {
        "user_id": 1,
        "date": "2024-02-02",
        "course_id": 1,
        "amount": 20000,
        "method": "T",
    },
    {
        "user_id": 1,
        "date": "2024-02-03",
        "lesson_id": 1,
        "amount": 10000,
        "method": "T",
    },
    {
        "user_id": 1,
        "date": "2024-02-04",
        "lesson_id": 2,
        "amount": 15000,
        "method": "C",
    },
    {
        "user_id": 1,
        "date": "2024-02-05",
        "lesson_id": 3,
        "amount": 20000,
        "method": "T",
    },
    {
        "user_id": 1,
        "date": "2024-02-06",
        "lesson_id": 4,
        "amount": 9000,
        "method": "T",
    }
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for test_payment in test_payments:
            payment = Payment.objects.create(**test_payment)
            payment.save()
        print('платежи были добавлены в базу данных')