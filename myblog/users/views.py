from django.shortcuts import render, redirect
from .forms import UserRegisterForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

def register(request):

    if request.method == 'POST':
        registerform = UserRegisterForm(request.POST) 
        
        if registerform.is_valid():
            registerform.save()
            
            username = registerform.cleaned_data.get('username')
            messages.success(request, "Your Account has been created!")

            return redirect('blog-login')
    else:
        registerform = UserRegisterForm()
    
    return render(request, 'users/register.html',{'registerform': registerform })

@login_required
def profile(request):
    user = request.user

    profile = ['hello']

    return render(request, 'users/profile.html',{'profile': profile})
