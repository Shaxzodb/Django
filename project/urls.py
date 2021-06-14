from django.urls import path
from .views import CreateViewPost

urlpatterns = [
    path('singup/',CreateViewPost.as_view(),name='singup')
    
]
