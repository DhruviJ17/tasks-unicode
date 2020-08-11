from django.db import models
# Create your models here.

class Num(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()

class ApiQuery(models.Model):
    username = models.CharField(max_length=200)
    repo_count = models.IntegerField(default=0)
    followers_count = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.username