from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название курса')
    image = models.ImageField(upload_to='skypro/', verbose_name='картинка для курсов', **NULLABLE)
    description = models.TextField(verbose_name='описание курса', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока', **NULLABLE)
    image = models.ImageField(upload_to='skypro/', verbose_name='картинка для урока', **NULLABLE)
    link_video = models.CharField(max_length=250, verbose_name='видео', **NULLABLE)
    course_title = models.ForeignKey('skypro.Course', verbose_name='урок из курса', on_delete=models.CASCADE,
                                     **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    CASH = 'cash'
    TRANSFER = 'transfer'
    PAYMENT_METHOD = (
        ('cash', 'наличные'),
        ('transfer', 'перевод')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты', **NULLABLE)
    paid_course = models.ForeignKey('skypro.Course', on_delete=models.CASCADE, verbose_name='оплаченный курс',
                                    **NULLABLE)
    paid_lesson = models.ForeignKey('skypro.Lesson', on_delete=models.CASCADE, verbose_name='оплаченный урок',
                                    **NULLABLE)
    payment_amount = models.FloatField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD, default=TRANSFER,
                                      verbose_name='способ оплаты')


class Subscription(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUSES = (
        ('active', 'Вы подписаны на курс'),
        ('inactive', 'Вы не подписаны на курс'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)
    course_id = models.ForeignKey('skypro.Course', verbose_name='курс', on_delete=models.CASCADE, **NULLABLE)
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус подписки', default=STATUS_INACTIVE)
