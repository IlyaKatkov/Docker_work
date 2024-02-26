from django.db import models

from django.db import models
from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    course_image = models.ImageField(upload_to='course', **NULLABLE, verbose_name='изображение')
    description = models.TextField(verbose_name='описание курса')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    price = models.PositiveIntegerField(default=1000, verbose_name='стоимость курса')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название урока')
    lesson_image = models.ImageField(upload_to='course', **NULLABLE, verbose_name='изображение')
    description = models.TextField(verbose_name='описание урока')
    link = models.CharField(max_length=200, verbose_name='ссылка')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')
    price = models.PositiveIntegerField(default=100, verbose_name='стоимость урока')

    def __str__(self):
        return f'Lesson - {self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
