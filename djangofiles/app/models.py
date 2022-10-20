from django.db import models

# Create your models here.
class password_model(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class password_storage(models.Model):
    stored_passwords = models.CharField(max_length=100)