from django.db import models

# Create your models here.
class register_model(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)

class log_in_model(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)