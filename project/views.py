
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreate



# Create your views here.
class CreateViewPost(CreateView):
    form_class=CustomUserCreate
    template_name='singup.html'
    success_url=reverse_lazy('login')
