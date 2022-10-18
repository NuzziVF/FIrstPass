from django import forms

class register_form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    repeat_password = forms.CharField(max_length=100)

class log_in_form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)