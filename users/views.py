from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Successfully created account for {username}')
            return redirect('index')
    else:
        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

def delete_account(request,id):
    try:
        u=User.objects.get(id=id)
        username=u.username
        u.delete()
        messages.success(request,f'successfully deleted account of {username}')
    except User.DoesNotExist:
        messages.error(request,"User not found")
    finally:
        return redirect('index')

class UserDeleteview(LoginRequiredMixin,DeleteView):
    model = User
    success_url = '/notes/'
    template_name='users/user_confirm_delete.html'

    # def test_func(self):
    #     account = self.get_object()
    #     if self.request.user == account.username:
    #         return True
    #     return False

    def post(self, request, *args, **kwargs):
        self.to_delete = self.request.POST.get('todelete')
        if  self.to_delete:
            user=self.get_object()
            username=user.username
            user.delete()
            messages.success(request,f'successfully deleted account {username}')
            return redirect('users-login')
        else:
            # return self.get(self, *args, **kwargs)
            return redirect('index')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username=u_form.cleaned_data.get('username')
            messages.success(request,f'successfully updated profile of {username}')
            return redirect('users-profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context ={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)


