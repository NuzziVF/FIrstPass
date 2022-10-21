from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from app.models import PasswordsModelForm
from django.forms import ModelForm

# from app.forms import Passwords


# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class NewBusinessForm(forms.Form):
    passwords_name = forms.CharField(label="Password Name", max_length=100)
    password_obj = forms.CharField(label="Password", max_length=100)


# class Passwords(forms.Form):
#     passwords_name = forms.CharField(required=True, max_length=30)
#     passwords = forms.CharField(required=True, max_length=50)

# class Meta:
# 	model = PasswordsModelForm
# 	fields = ('passwords_name', 'password_obj')
