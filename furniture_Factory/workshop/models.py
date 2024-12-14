from django.db import models
from django.db.models.signals import post_save, post_delete
from django.conf import settings
from django.core.exceptions import ValidationError
import re

from django.dispatch import receiver


def validate_time_range(value):
    # Регулярное выражение для формата времени HH:MM-HH:MM
    time_pattern = r"^([01]?[0-9]|2[0-3]):([0-5][0-9])\-([01]?[0-9]|2[0-3]):([0-5][0-9])$"
    match = re.match(time_pattern, value)
    if not match:
        raise ValidationError("Неверный формат времени. Используйте формат HH:MM-HH:MM.")

    # Проверка, что время начала не позже времени окончания
    start_time = value.split('-')[0]
    end_time = value.split('-')[1]

    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))

    if (start_hour > end_hour) or (start_hour == end_hour and start_minute > end_minute):
        raise ValidationError("Время окончания не может быть раньше времени начала.")

STATUS_CHOICES = [
    ('working', 'Работает'),
    ('on_leave', 'В отпуске'),
    ('fired', 'Уволен'),
]

class Worker(models.Model):
    fullName = models.CharField(max_length=256, verbose_name='ФИО рабочего')
    dateBirth = models.DateField(verbose_name='Дата рождения')
    workshop = models.ForeignKey(
        'Workshop',
        verbose_name='Цех',
        related_name='workers',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='working',
        verbose_name='Статус'
    )
    workingHours = models.CharField(
        max_length=11,
        verbose_name='Рабочие часы',
        validators=[validate_time_range]
    )

    class Meta:
        verbose_name = 'работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.fullName

class Workshop(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название места')
    supervisor = models.OneToOneField(
        Worker,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='workshop_supervised',
        verbose_name='Начальник цеха')
    description = models.TextField(verbose_name='Описание')
    numberWorkers = models.IntegerField(default=0, verbose_name='Количество работников')

    class Meta:
        verbose_name = 'цех'
        verbose_name_plural = 'Цехи'

    def __str__(self):
        return self.name

# Сигнал обновления количества работников при добавлении
@receiver(post_save, sender=Worker)
def update_worker_count_on_save(sender, instance, **kwargs):
    workshop = instance.workshop
    workshop.numberWorkers = workshop.workers.count()
    workshop.save()


# Сигнал обновления количества работников при удалении
@receiver(post_delete, sender=Worker)
def update_worker_count_on_delete(sender, instance, **kwargs):
    workshop = instance.workshop
    workshop.numberWorkers = workshop.workers.count()
    workshop.save()
