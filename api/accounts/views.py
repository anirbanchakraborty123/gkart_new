from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .forms import RegistrationForm
from .models import Account
# Create your views here.

def Register(request):
    if request.method=='POST':
        form= RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            email      = form.cleaned_data['email']
            phoneno    = form.cleaned_data['phoneno']
            password   = form.cleaned_data['password']
            username   = email.split('@')[0]
            user       = Account.objects.Create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.phoneno= phoneno
            user.is_active= True
            user.save()
            if user:
                return redirect('login')
        
    else:
        form= RegistrationForm()

    context={
        'form': form
    }
    return render(request, 'accounts/register.html',context)

def Login(request):
    return render(request, 'accounts/login.html')

def Logout(request):
    pass