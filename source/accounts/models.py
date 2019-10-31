from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class GitHubUser(models.Model):
    user = models.OneToOneField(User, default='Не указано', on_delete=models.CASCADE, related_name='github_link', null=True)
    link = models.URLField(verbose_name='Ссылка на гитхаб',max_length=256)

    def __str__(self):
        return self.link