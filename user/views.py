from django.shortcuts import render
from django.views import View
# Create your views here.

def Register(request):
    return render(request, 'user/register.html')

def LoginView(request):
    return render(request, 'user/login.html')

