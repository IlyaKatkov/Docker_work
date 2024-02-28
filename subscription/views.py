from rest_framework.views import APIView
from rest_framework.response import Response
from materials.models import Course
from subscription.models import Subscription
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    user = openapi.Parameter('user', openapi.IN_QUERY, description="user_id", type=openapi.TYPE_NUMBER)
    course = openapi.Parameter('course', openapi.IN_QUERY, description="course_id", type=openapi.TYPE_NUMBER)

    @swagger_auto_schema(operation_description="Эта точка позволяет создавать и удалять подписку",
                         manual_parameters=[user, course], responses={200: 'Subscription deleted/Subscription created'})

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data["course"]
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user).filter(course=course_id).all()

        if len(subs_item) > 0:
            subscription_id = subs_item[0].pk
            subscription = Subscription.objects.get(pk=subscription_id)
            subscription.delete()
            message = 'Subscription deleted'
        else:
            new_subscription = {
                "user": user,
                "course_id": course_id
            }
            Subscription.objects.create(**new_subscription)
            message = 'Subscription created'
        return Response({"message": message})
