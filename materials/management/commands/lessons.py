from django.core.management import BaseCommand
from materials.models import Course, Lesson


test_course = {
        "name": "Course 1 Test",
        'description': "Test description for course 1",
        "user_id": 1
    }



test_lessons = [
    {
        "user_id": 1,
        "name": "Lesson 1",
        "description": "Decsription for lesson 1",
        "link": "www.testlink1.com",
        "course_id": 1,
    },
    {
        "user_id": 1,
        "name": "Lesson 2",
        "description": "Decsription for lesson 2",
        "link": "www.testlink2.com",
        "course_id": 1,
    },
    {
        "user_id": 1,
        "name": "Lesson 3",
        "description": "Decsription for lesson 3",
        "link": "www.testlink3.com",
        "course_id": 1,
    },
    {
        "user_id": 1,
        "name": "Lesson 4",
        "description": "Decsription for lesson 4",
        "link": "www.testlink4.com",
        "course_id": 1,
    },
    {
        "user_id": 1,
        "name": "Lesson 5",
        "description": "Decsription for lesson 5",
        "link": "www.testlink5.com",
        "course_id": 1,
    },
    {
        "user_id": 1,
        "name": "Lesson 6",
        "description": "Decsription for lesson 6",
        "link": "www.testlink6.com",
        "course_id": 1,
    },
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        course = Course.objects.create(**test_course)
        course.save()
        for test_lesson in test_lessons:
            lesson = Lesson.objects.create(**test_lesson)
            lesson.save()
        print('Уроки были добавлены в базу данных')