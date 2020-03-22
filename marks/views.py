from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,UpdateView,CreateView
from .models import Sem1,Sem2
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.

class SemOneListView(LoginRequiredMixin,ListView):
    model=Sem1
    template_name='marks/sem_list.html'
    context_object_name='sem_list'
    def get_queryset(self):
        return Sem1.objects.filter(user=self.request.user).first()

class SemTwoListView(LoginRequiredMixin,ListView):
    model=Sem2
    template_name='marks/sem_list.html'
    context_object_name='sem_list'
    def get_queryset(self):
        return Sem2.objects.filter(user=self.request.user).first()   

def total_marks(request):
    sem1=Sem1.objects.filter(user=request.user).first()  
    sem2=Sem2.objects.filter(user=request.user).first()  
    context={}
    context['sem1']=sem1
    context['sem2']=sem2
    return render(request,"marks/total_list.html",context)

class SemOneUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Sem1
    success_url='/marks/sem-one/'
    fields =['m1','ppsc','ep','bee','eng','es']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        sem1 = self.get_object()
        if self.request.user == sem1.user:
            if self.request.method=='POST':
                messages.success(self.request,f'successfully updated memo of :{sem1.user}-sem(1) ')
            return True

class SemTwoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Sem2
    success_url='/marks/sem-two/'
    fields =['m2','ds_c','ec','ed','em','es']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        sem2 = self.get_object()
        if self.request.user == sem2.user:
            if self.request.method=='POST':
                messages.success(self.request,f'successfully updated memo of :{sem2.user}-sem(2) ')
            return True



# class SemUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
#     model=Memo
#     success_url='/sem/'
#     fields =['sem','sub1','sub2','sub3']
    
#     def form_valid(self,form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#     def test_func(self):
#         memo = self.get_object()
#         if self.request.user == memo.user:
#             if self.request.method=='POST':
#                 messages.success(self.request,f'successfully updated memo of :{memo.user}-sem({memo.sem}) ')
#             return True


