from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomUser,SomeLocationModel
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from mapbox_location_field.admin import MapAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(SomeLocationModel, MapAdmin)
