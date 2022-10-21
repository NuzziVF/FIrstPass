from django.db import models
from django.forms import CharField, ModelForm

# Create your models here.


class PasswordsModel(models.Model):
    passwords_name = models.CharField(max_length=30)
    password_obj = models.CharField(max_length=50)


class Listing(models.Model):
    # username = models.CharField(max_length=30)
    passwords_name = models.CharField(max_length=80)
    password_obj = models.CharField(max_length=80)

    def __str__(self):
        return self.passwords_name


# class PasswordsModelForm(ModelForm):
#     class Meta:
#         model = PasswordsModel
#         fields = ['passwords_name', 'password_obj']
