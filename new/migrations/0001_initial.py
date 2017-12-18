# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScanDrivers',
            fields=[
                ('id_driver', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='id пилота')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('nat', models.CharField(max_length=100, verbose_name='Национальность')),
                ('oa', models.IntegerField(verbose_name='Уровень')),
                ('con', models.IntegerField(verbose_name='Концентрация')),
                ('tal', models.IntegerField(verbose_name='Талант')),
                ('exp', models.IntegerField(verbose_name='Опыт')),
                ('agg', models.IntegerField(verbose_name='Агрессивность')),
                ('tei', models.IntegerField(verbose_name='Технические знания')),
                ('sta', models.IntegerField(verbose_name='Выносливость')),
                ('cha', models.IntegerField(verbose_name='Харизма')),
                ('mot', models.IntegerField(verbose_name='Мотивация')),
                ('rep', models.IntegerField(verbose_name='Репутация')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('wei', models.IntegerField(verbose_name='Вес')),
                ('ret', models.IntegerField(verbose_name='Заканчивает карьеру')),
                ('sal', models.IntegerField(verbose_name='Зарплата')),
                ('fee', models.IntegerField(verbose_name='Премия')),
                ('fav', models.CharField(max_length=100, verbose_name='id любимых трасс')),
                ('off', models.IntegerField(verbose_name='Предложений работы')),
                ('date', models.CharField(max_length=100, verbose_name='Время скачивания списка')),
            ],
        ),
    ]