from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomAuthenticationForm, NewUserForm


def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Вы успешно вошли в свой аккаунт")
                return redirect("home")
            else:
                messages.error(request,"Неправильный логин или пароль.")
        else:
            messages.error(request,"Неправильный логин или пароль.")
            
    form = CustomAuthenticationForm()
    return render(request, 'profiles/login.html', { "login_form":form })

def logout(request):
    auth_logout(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Вы успешно зарегистрировались." )
            return redirect("home")
        messages.error(request, "Неудачная регистрация. Неверная информация.")
    form = NewUserForm()
    return render (request=request, template_name="profiles/register.html", context={"register_form":form})
