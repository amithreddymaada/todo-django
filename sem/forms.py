from django import forms
from django.contrib.auth.models import User
from .models import Memo



class SemWiseMemoForm(forms.ModelForm):
    class Meta:
        model=Memo
        fields=['user','sem','sub1','sub2','sub3']

