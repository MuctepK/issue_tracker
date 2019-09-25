from django.db import models


class Issue(models.Model):
    summary = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, verbose_name='Статус', related_name='issues')
    type = models.ForeignKey('webapp.Type', on_delete=models.PROTECT, verbose_name='Тип', related_name='issues')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.summary[:20]


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name



