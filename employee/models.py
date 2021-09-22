from django.db import models
from company.models import Department


POST_TYPES = [
    ('MN', 'Manager'),
    ('SB', 'Subordinate'),
]


class Employee(models.Model):
    '''
    Модель сотрудника компании
    '''
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    patronymic = models.CharField(max_length=128, verbose_name='Отчество')
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Отдел'
    )
    post = models.CharField(max_length=255, verbose_name='Должность')
    post_type = models.CharField(max_length=20, choices=POST_TYPES, verbose_name='Тип должности')

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
