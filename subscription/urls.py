from subscription.apps import SubscriptionConfig
from django.urls import path
from subscription.views import SubscriptionAPIView


app_name = SubscriptionConfig.name

urlpatterns = [
    path('subscription/', SubscriptionAPIView.as_view(), name='subscription'),
]