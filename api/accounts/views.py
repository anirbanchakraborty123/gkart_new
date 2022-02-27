from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.http import HttpResponse, request
from .forms import RegistrationForm
from .models import Account
import time
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
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
                messages.success(request,"Registration Successful")
                return redirect('register')
        
    else:
        form= RegistrationForm()

    context={
        'form': form
    }
    return render(request, 'accounts/register.html',context)

def Login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user= auth.authenticate(email=email,password=password)
        if user is not None:
            rs=request.session["uid"]=user.id
            auth.login(request,user)
            # print(user.first_name)
            return redirect('home')
        else:
            messages.error(request,"Wrong Credantials")
            return redirect('login')

        
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Logout(request):
    # pass
    auth.logout(request)
    messages.success(request,"Logged Out Successfully ")
    return redirect('login')