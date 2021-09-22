from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


ORGANIZATIONS_LEVELS = [
    ('1', '1-й уровень'),
    ('2', '2-й уровень'),
    ('3', '3-й уровень'),
    ('4', '4-й уровень'),
    ('5', '5-й уровень'),
]


def min_max_validate(value):
    '''
    Проверяет максимальное и минимальное значение
    '''
    if (value < 1) and (value > 5):
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


class Company(models.Model):
    '''
    Модель компании
    '''
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Department(models.Model):
    '''
    Модель подразделения (отдела)
    '''
    name = models.CharField(max_length=255, verbose_name='Название')
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Компания'
    )
    level = models.CharField(
        max_length=30,
        choices=ORGANIZATIONS_LEVELS,
        verbose_name='Уровень в организации',
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class HighLevelDepartment(models.Model):
    '''
    Модель является прослойкой между подразделениями, для удобства
    работы подчиненности. Это самое быстрое решение, но не самое правильное
    '''
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Подразделение'
    )

    def __str__(self):
        return self.department.__str__()


class DepartmentRelations(models.Model):
    '''
    Модель для обеспечение подчиненности одних подразделений другим
    '''
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Отдел'
    )
    high_level_department = models.ForeignKey(
        HighLevelDepartment,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Кому подчиняется'
    )

    def __str__(self):
        return self.department.__str__()

    class Meta:
        verbose_name = 'Схема подчинения'
        verbose_name_plural = 'Схемы подчинения'
