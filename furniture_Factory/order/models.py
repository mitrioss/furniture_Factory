from django.db import models

from workshop.models import Workshop


class StatusOrder(models.Model):
    nameStatus = models.CharField(max_length=10, verbose_name='Название статуса')

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.nameStatus

class Order(models.Model):
    orderNumber = models.IntegerField(verbose_name='Номер заказа', unique=True)
    startDate = models.DateField(verbose_name='Дата начала')
    endDate = models.DateField(verbose_name='Дата окончания')
    status = models.ForeignKey(StatusOrder, verbose_name='Статус')
    workshops = models.ForeignKey(Workshop, verbose_name='Цех', blank=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.orderNumber
