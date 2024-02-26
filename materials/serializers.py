from rest_framework import serializers
from materials.models import Course, Lesson
from materials.validators import wrong_links_validator
from subscription.models import Subscription


class LessonsSerializer(serializers.ModelSerializer):
    link = serializers.CharField(validators=[wrong_links_validator])

    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "link"]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    course_subscription = serializers.SerializerMethodField()
    lessons = LessonsSerializer(source="lesson_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name", "description", "count_lessons", "lessons", "course_subscription"]

    def get_count_lessons(self, instance):
        return len(Lesson.objects.all().filter(course=instance.pk))

    def get_course_subscription(self, instance):
        subscription = Subscription.objects.all().filter(course=instance.pk).filter(user=self.context.get('request').user.pk)
        if subscription:
            return True
        else:
            return False



class LessonSerializer(serializers.ModelSerializer):
    link = serializers.CharField(validators=[wrong_links_validator])

    class Meta:
        model = Lesson
        fields = '__all__'