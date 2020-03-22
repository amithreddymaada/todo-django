from django import forms
from django.contrib.auth.models import User
from .models import Sem1,Sem2



class SemOneMemoForm(forms.ModelForm):
    class Meta:
        model=Sem1
        fields=['user','m1','ppsc','bee','ep','eng','es']

class SemTwoMemoForm(forms.ModelForm):
    class Meta:
        model=Sem2
        fields=['user','m2','ds_c','ec','ed','em','es']