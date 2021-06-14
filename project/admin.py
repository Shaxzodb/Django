from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreate,CustomUserChange
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreate
    form=CustomUserChange
    model=CustomUser
    list_display=['username','email','yosh','address']
admin.site.register(CustomUser,CustomUserAdmin)
