from .views import BoshSahifa
from django.urls import path

urlpatterns = [
    path('',BoshSahifa.as_view(),name='home')
]
