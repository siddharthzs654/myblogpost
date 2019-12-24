from django.shortcuts import render, redirect
from .forms import UserRegisterForm

from django.contrib import messages
# Create your views here.

def register(request):

    if request.method == 'POST':
        registerform = UserRegisterForm(request.POST) 
        
        if registerform.is_valid():
            registerform.save()
            
            username = registerform.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")

            return redirect('blog-home')
    else:
        registerform = UserRegisterForm()
    
    return render(request, 'users/register.html',{'registerform': registerform })

