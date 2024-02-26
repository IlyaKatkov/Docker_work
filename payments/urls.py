from payments.views import PaymentListAPIView
from payments.apps import PaymentsConfig
from django.urls import path

# Описание маршрутизации для ViewSet

app_name = PaymentsConfig.name

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
]