from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,UpdateView,CreateView
from .models import Memo
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import SemWiseMemoForm

# Create your views here.

class SemListView(LoginRequiredMixin,ListView):
    model=Memo
    template_name='sem/index.html'
    def get_queryset(self):
        return Memo.objects.filter(user=self.request.user).order_by('sem')
    

class SemCreateView(LoginRequiredMixin,CreateView):
    model=Memo
    success_url='/sem/'
    fields =['sem','sub1','sub2','sub3']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def sem_marks(request,sem):
    memo_list=Memo.objects.filter(sem=sem).filter(user=request.user)
    return render(request,'sem/sem_marks.html',{'memo_list':memo_list})

class SemUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Memo
    success_url='/sem/'
    fields =['sem','sub1','sub2','sub3']
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
        memo = self.get_object()
        if self.request.user == memo.user:
            if self.request.method=='POST':
                messages.success(self.request,f'successfully updated memo of :{memo.user}-sem({memo.sem}) ')
            return True




def sem_update(request,id):
    if request.method == 'POST':
        form=SemWiseMemoForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('user')
            messages.success(request,f'Successfully updated memo of: {username}!')
            return redirect('sem-index')
    else:
        form=SemWiseMemoForm(instance=request.user)
    memo=Memo.objects.get(id=id)
    heading=Memo.objects.filter(sem=memo.sem).first()
    return render(request,'sem/memo_update.html',{'form':form,'heading':heading})
    
    




