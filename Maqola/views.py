from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from .models import Article
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView


class AlerDetailViewsPot(LoginRequiredMixin,DetailView):
    model=Article
    template_name='detail.html'
    login_url='login'
    
class AlerListViewPost(LoginRequiredMixin,ListView):
    model=Article
    template_name='article.html'
    """ context_object_name="Postlar" """
    login_url='login'
class AlerCreateViews(LoginRequiredMixin,CreateView):
    model=Article
    template_name='new.html'
    fields=('title','photo','text','kurish')
    success_url=reverse_lazy('article')
    login_url='login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AlerDeleteViews(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Article
    template_name='delete.html'
    fields=('title','text','author','date','photo','kurish')
    success_url=reverse_lazy('article')
    login_url='login'

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user
class AlerUpdateViews(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Article
    template_name='update.html'
    fields=('title','text','photo','kurish')
    success_url=reverse_lazy('article')
    login_url='login'
    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user
    
