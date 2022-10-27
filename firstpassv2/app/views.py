from django.shortcuts import render, redirect
from pyparsing import Optional
from .forms import NewUserForm, NewBusinessForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from app.models import Listing

# class DiagramsPageView(TemplateView):
#     template_name = 'base.html'

#     def get_context_data(self, **kwargs):
#         context = super(DiagramsPageView, self).get_context_data(**kwargs)
#         context['posts'] = Passwords.objects.all()
#         return context


def new_business(request):
    if request.method == "POST":
        form = NewBusinessForm(request.POST)
        if form.is_valid():
            obj = Listing()  # gets new object
            obj.passwords_name = form.cleaned_data["passwords_name"]
            obj.password_obj = form.cleaned_data["password_obj"]
            obj.save()
            return HttpResponseRedirect("/")
    else:
        form = NewBusinessForm()

    return render(request, "base.html", {"form": form})


def get_data(request):

    my_data = Listing.objects.all()  # for all the records
    one_data = Listing.objects.get(
        pk=1
    )  # 1 will return the first item change it depending on the data you want
    context = {
        "my_data": my_data,
        "one_data": one_data,
    }

    return render(request, "get_data.html", context)


# class newBusiness(FormView):
#     form_class = NewBusinessForm
#     success_url = "/"
#     template_name = "temp.html"

#     def form_valid(self, form):
#         form.save()
#         return redirect(self.success_url)


# def homepage(request):
#     # args = {}
#     if request.method == "POST":
#         form = Passwords(request.POST)
#         if form.is_valid():
#             # text = form.cleaned_data['password_name']
#             pass
#         # args = {'form': form, 'text': text}

#     else:
#         form = Passwords()

#     return render(request=request, template_name="base.html", context={"form": form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request, template_name="signup.html", context={"register_form": form}
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request, template_name="login.html", context={"login_form": form}
    )


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")
