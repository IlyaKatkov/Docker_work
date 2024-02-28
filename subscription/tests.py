from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from subscription.models import Subscription
from materials.models import Course


class SubscriptionAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            name="testuser",
            email="testuser@test,com",
            phone_number="12345",
            city="testcity",
            password='12345'
        )
        self.course = Course.objects.create(
            id=10,
            name="CourseTest 1",
            description="CourseDescroption1",
            user=self.user
        )

    def test_create_subscription(self):
        data = {
            "user": self.user.pk,
            "course": self.course.pk
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/subscription/',
            data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
