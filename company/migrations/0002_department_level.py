# Generated by Django 3.2.7 on 2021-09-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='level',
            field=models.IntegerField(default=1, help_text='Укажите уровень отделав рамках компании (от 1 до 5)', verbose_name='Уровень в организации'),
        ),
    ]
