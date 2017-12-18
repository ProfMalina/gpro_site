from django.db import models


class ScanDrivers(models.Model):
    id_driver = models.IntegerField(verbose_name='id пилота', primary_key=True, default=0)
    name = models.CharField(verbose_name='Имя', max_length=100)
    nat = models.CharField(verbose_name='Национальность', max_length=100)
    oa = models.IntegerField(verbose_name='Уровень')
    con = models.IntegerField(verbose_name='Концентрация')
    tal = models.IntegerField(verbose_name='Талант')
    exp = models.IntegerField(verbose_name='Опыт')
    agg = models.IntegerField(verbose_name='Агрессивность')
    tei = models.IntegerField(verbose_name='Технические знания')
    sta = models.IntegerField(verbose_name='Выносливость')
    cha = models.IntegerField(verbose_name='Харизма')
    mot = models.IntegerField(verbose_name='Мотивация')
    rep = models.IntegerField(verbose_name='Репутация')
    age = models.IntegerField(verbose_name='Возраст')
    wei = models.IntegerField(verbose_name='Вес')
    ret = models.IntegerField(verbose_name='Заканчивает карьеру')
    sal = models.IntegerField(verbose_name='Зарплата')
    fee = models.IntegerField(verbose_name='Премия')
    fav = models.CharField(verbose_name='id любимых трасс', max_length=100)
    off = models.IntegerField(verbose_name='Предложений работы')
    date = models.CharField(verbose_name='Время скачивания списка', max_length=100)
