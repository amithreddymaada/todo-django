from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Memo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    sem=models.IntegerField()
    sub1=models.CharField(max_length=100)
    sub2=models.CharField(max_length=100)
    sub3=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user}\'s sem-{self.sem} '







