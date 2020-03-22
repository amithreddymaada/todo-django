from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Remainder
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,"notes/about.html")


class RemainderListView(LoginRequiredMixin,ListView):
    model = Remainder
    template_name = 'notes/index.html'
    context_object_name = 'remainders'
    paginate_by = 3
    def get_queryset(self):
        return Remainder.objects.filter(end_date__gte=timezone.now()).all().order_by('-created_date')

class UserRemainderListView(LoginRequiredMixin,ListView):
    model = Remainder
    template_name = 'notes/user_remainders.html'
    context_object_name = 'remainders'
    paginate_by = 3
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Remainder.objects.filter(user=user).filter(end_date__gte=timezone.now()).all().order_by('-created_date')


# def remainderlistview(request):
#     remainders = Remainder.objects.filter(end_date__gte=timezone.now()).all()
#     context ={'remainders':remainders}
#     return render(request,'notes/index.html',context)

def remove_outdated(request):
    remove_note=Remainder.objects.filter(end_date__lte=timezone.now()).all()
    for note in remove_note:
        note.delete()
    remainders = Remainder.objects.filter(end_date__gte=timezone.now()).all().order_by('-created_date')
    paginate_by=3
    context={'remainders':remainders}
    return render(request,'notes/index.html',context)


class RemainderDetailView(LoginRequiredMixin,DetailView):
    model  = Remainder

class RemainderCreateView(LoginRequiredMixin,CreateView):
    model = Remainder
    success_url='/notes/'
    fields =['title','note','end_date']
    

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RemainderUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Remainder
    fields =['title','note','end_date']
    
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            if self.request.method=='POST':
                messages.success(self.request,f'successfully updated remainder: ')
            return True
        return False

class RemainderDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Remainder
    success_url = '/notes/'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True
        return False
    def post(self, request, *args, **kwargs):
        self.to_delete = self.request.POST.get('todelete')
        if  self.to_delete:
            note=self.get_object()
            title=note.title
            note.delete()
            messages.success(request,f'successfully deleted remainder: {title}')
            return redirect('index')
        else:
            return self.get(self, *args, **kwargs)
        



