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
# def get_user_ip_details(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
    
#     device_type = ""
#     browser_type = ""
#     browser_version = ""
#     os_type = ""
#     os_version = ""
#     if request.user_agent.is_mobile:
#         device_type = "Mobile"
#     if request.user_agent.is_tablet:
#         device_type = "Tablet"
#     if request.user_agent.is_pc:
#         device_type = "PC"
    
#     browser_type = request.user_agent.browser.family
#     browser_version = request.user_agent.browser.version_string
#     os_type = request.user_agent.os.family
#     os_version = request.user_agent.os.version_string
#     context = {
#         "ip": ip,
#         "device_type": device_type,
#         "browser_type": browser_type,
#         "browser_version": browser_version,
#         "os_type":os_type,
#         "os_version":os_version
#     }
#     return context