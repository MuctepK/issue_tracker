from django.db import models
DEFAULT_STATUS_ID = 1
DEFAULT_TYPE_ID = 1
PROJECT_DEFAULT_STATUS = 'active'
PROJECT_STATUS_CHOICES = [
    ('active', 'Активный'),
    ('closed', 'Закрыт')
]


class Issue(models.Model):
    summary = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, blank=False, default=DEFAULT_STATUS_ID,
                               verbose_name='Статус', related_name='issues')
    type = models.ForeignKey('webapp.Type', on_delete=models.PROTECT, blank=False, default=DEFAULT_TYPE_ID,
                             verbose_name='Тип', related_name='issues')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, blank=False, null=True, related_name='issue')

    def __str__(self):
        return self.summary[:20]


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=50, verbose_name='Статус', default=PROJECT_DEFAULT_STATUS,
                              choices=PROJECT_STATUS_CHOICES)

    def __str__(self):
        return self.name[:30]

class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name



