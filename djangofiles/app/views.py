from django.shortcuts import  render, redirect
from .forms import register_form, log_in_form
from .models import password_model
# Create your views here.

def register(request):
    form = register_form(request.GET)
    if form.is_valid():
        obj = password_model()
        obj.username = form.cleaned_data["username"]
        obj.password1 = form.cleaned_data["password1"]
        obj.password2 = form.cleaned_data["password2"]
        if obj.password1 == obj.password2:
            obj.save()
        context = {"form":form, "username":obj.username, "password1":obj.password1,"password2":obj.password2}
        return redirect(f'/log_in/')
    else: 
        context = {"form":form}
        return render(request, "register.html", context)

def log_in(request):
    form = log_in_form(request.GET)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        verification_username = password_model.objects.get(username=username)
        verification_password = password_model.objects.get(password=password)
        if verification_username == username and verification_password == password:
            return redirect(f'/home/{username}') 
        else:
            error = "Wrong password or username"
            context = {"form":form, "error":error}
        return render(request, "log_in.html", context)
    else:
        context = {"form":form}
        return render(request, "log_in.html", context)

def home(request, username):
    verification_username = password_model.objects.get(username=username)
    passwords = password_model.objects.filter()
    context = {"verification_username": verification_username}
    return render(request, "home.html", context)
