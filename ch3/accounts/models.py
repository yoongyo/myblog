from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=20)
    adress = models.CharField(max_length=50)