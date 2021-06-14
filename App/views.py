from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import TemplateView,ListView
# Create your views here.
class BoshSahifa(LoginRequiredMixin,TemplateView):
    template_name='home.html'
    login_url='login'
