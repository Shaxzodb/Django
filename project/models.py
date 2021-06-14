from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    yosh=models.PositiveIntegerField(null=True,blank=True)
    address=models.CharField('Author',max_length=100)
    email=models.EmailField()
