from django.db import models


class SiteDrv(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=100)
    text = models.TextField(verbose_name=u'Контент')
    create_data = models.DateTimeField()
