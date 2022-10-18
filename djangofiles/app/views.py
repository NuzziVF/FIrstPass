from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from http.client import HTTPResponse
from .forms import register_form, log_in_form

# Create your views here.
def register(request):
    form = register_form(request.GET)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        repeat_password = form.cleaned_data["repeat_password"]
        context = {"form":form, "username":username, "password":password,"repeat_password":repeat_password}
        return render(request, "hey_you.html", context)
    else: 
        context = {"form":form}
        return render(request, "hey_you.html", context)

def log_in(request):
    form = log_in_form(request.GET)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        context = {"form":form, "username":username, "password":password}
        return render(request, "hey_you.html", context)
    else: 
        context = {"form":form}
        return render(request, "hey_you.html", context)