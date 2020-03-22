from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Remainder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    note = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Remainder'
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return reverse('posts-detail',args=(self.id,))
        return reverse('detail',kwargs ={'pk':self.pk})
        


    