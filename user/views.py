from django.shortcuts import render, redirect
from django.views import View
from .form import LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

def RegisterView(request):
    return render(request, 'user/register.html')

def LoginView(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home")
    return render(request, 'user/login.html', context)

