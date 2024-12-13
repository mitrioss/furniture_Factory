from django.db import models
from django.db.models.signals import post_save, post_delete
from django.conf import settings
from django.dispatch import receiver


STATUS_CHOICES = [
    ('working', 'Работает'),
    ('on_leave', 'В отпуске'),
    ('fired', 'Уволен'),
]

class Workshop(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название места')
    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='workshop_supervised')
    description = models.TextField(verbose_name='Описание')
    numberWorkers = models.IntegerField(default=0, verbose_name='Количество работников')

    class Meta:
        verbose_name = 'цех'
        verbose_name_plural = 'Цехи'

    def __str__(self):
        return self.name

class Worker(models.Model):
    fullName = models.CharField(max_length=256, verbose_name='ФИО рабочего')
    dateBirth = models.DateField(verbose_name='Дата рождения')
    workshop = models.ForeignKey(
        Workshop,
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
        verbose_name='Рабочие часы'
    )

    class Meta:
        verbose_name = 'работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.fullName

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
