from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название курса')
    image = models.ImageField(upload_to='skypro/', verbose_name='картинка для курсов', **NULLABLE)
    description = models.TextField(verbose_name='описание курса', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока', **NULLABLE)
    image = models.ImageField(upload_to='skypro/', verbose_name='картинка для урока', **NULLABLE)
    link_video = models.FileField(upload_to='skypro/', verbose_name='видео', **NULLABLE)
    course_title = models.ForeignKey('skypro.Course', verbose_name='урок из курса', on_delete=models.CASCADE,
                                     **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
