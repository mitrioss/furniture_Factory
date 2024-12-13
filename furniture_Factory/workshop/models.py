from django.db import models
from django.contrib.auth import get_user_model
from users.models import User

User = get_user_model()

STATUS_CHOICES = [
    ('working', 'Работает'),
    ('on_leave', 'В отпуске'),
    ('fired', 'Уволен'),
]

class Workshop(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название места')
    supervisor = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='workshop_supervised')
    description = models.TextField(verbose_name='Описание')
    numberWorkers = models.IntegerField(verbose_name='Количество работников')

    class Meta:
        verbose_name = 'цех'
        verbose_name_plural = 'Цехи'

    def __str__(self):
        return self.name

class Worker():
    fullName = models.CharField(max_length=256, verbose_name='ФИО рабочего')
    dateBirth = models.DateField(verbose_name='Дата рождения')
    workshop = models.ForeignKey(
        Workshop,
        verbose_name='Цех',
        related_name='workers'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='working',
        verbose_name='Статус'
    )
    workingHours = models.CharField(
        max_length=11,
        verbose_name='Рабочие часы'
    )

    class Meta:
        verbose_name = 'работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.fullName