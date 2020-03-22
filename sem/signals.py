from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import  Memo
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Memo.objects.create(user=instance,sem=1,sub1='M1',sub2='BEE',sub3='EP')
        Memo.objects.create(user=instance,sem=2,sub1='M2',sub2='CHEMISTRY',sub3='DS')

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    for sem_memo in instance.memo_set.all():
        sem_memo.save()



    