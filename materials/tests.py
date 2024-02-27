from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from materials.models import Course, Lesson
from users.models import User



class CourseAPITest(APITestCase):

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
        self.lesson = Lesson.objects.create(
            id=1,
            name="LessonTest 1",
            description="Lesson DiscriptionTest",
            link="youtube.com",
            course=self.course,
            user=self.user
        )

    def test_get_list_course(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/course/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_course(self):
        data = {
            "name": "CourseTest 2",
            "description": "CourseDescroption2",
            "user": self.user
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/course/',
            data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_course(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            '/course/10/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_get_list_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/lesson/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        data = {
            "name": "LessonTest 2",
            "description": "Lesson DiscriptionTest2",
            "user": self.user,
            "link": "youtube.com",
        }
        print(data)
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/course/',
            data=data)
        print(response)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            '/lesson/delete/1/')
        print(Lesson.objects.all())

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )