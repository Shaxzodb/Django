from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=256)
    text=models.TextField()
    photo=models.ImageField(upload_to='images/',blank=True)
    date=models.DateTimeField(auto_now_add=True)
    kurish=models.PositiveIntegerField(null=True, blank=True)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title[:80]+'...'
    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
    
