from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email', 'ssn','first_name','last_name','address','phone','gender','image')

class CustomUserChangeForm(UserChangeForm):

    class Meta():
        model = CustomUser
        fields = ('username','email')
