from django.db import models

from workshop.models import Workshop


STATUS_CHOICES = [
    ('admin', 'Администратор'),
    ('supervisor', 'Начальник цеха'),
    ('worker', 'Рабочий'),
]

class Order(models.Model):
    orderNumber = models.IntegerField(
        verbose_name='Номер заказа',
        unique=True
    )
    startDate = models.DateField(verbose_name='Дата начала')
    endDate = models.DateField(verbose_name='Дата окончания')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='working',
        verbose_name='Статус'
    )
    workshops = models.ForeignKey(
        Workshop,
        verbose_name='Цех',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.orderNumber
