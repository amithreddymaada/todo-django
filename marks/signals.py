from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import  Sem1,Sem2
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Sem1.objects.create(user=instance,m1='#',ppsc='',ep='',bee='',eng='',es='')
        Sem2.objects.create(user=instance,m2='#',ds_c='',ec='',ed='',em='',es='')
        

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.sem1.save()
    instance.sem2.save()