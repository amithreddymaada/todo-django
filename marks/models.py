from django.db import models
from django.contrib.auth.models import User

class Sem2(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    m2=models.CharField(max_length=20)
    ds_c=models.CharField(max_length=20)
    ec=models.CharField(max_length=20)
    ed=models.CharField(max_length=20)
    em=models.CharField(max_length=20)
    es=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user}\'s sem-2 '

class Sem1(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    m1=models.CharField(max_length=1)
    ppsc=models.CharField(max_length=1)
    ep=models.CharField(max_length=1)
    bee=models.CharField(max_length=1)
    eng=models.CharField(max_length=1)
    es=models.CharField(max_length=1)

    def __str__(self):
        return f'{self.user}\'s sem-1 '
