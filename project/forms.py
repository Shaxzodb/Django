
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreate(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('yosh','address','email')
class CustomUserChange(UserChangeForm):
    class Meta(UserChangeForm):
        model=CustomUser
        fields=UserChangeForm.Meta.fields