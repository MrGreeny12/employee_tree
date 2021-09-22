# Generated by Django 3.2.7 on 2021-09-21 16:46

import company.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_department_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='level',
            field=models.IntegerField(default=1, help_text='Укажите уровень отдела в рамках компании (от 1 до 5)', validators=[company.models.min_max_validate], verbose_name='Уровень в организации'),
        ),
    ]
