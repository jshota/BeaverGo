from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,SomeLocationModel
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email', 'ssn','first_name','last_name','address','phone','gender','image')

class CustomUserChangeForm(UserChangeForm):

    class Meta():
        model = CustomUser
        fields = ('username','email')


class LocationForm(forms.ModelForm):
    class Meta:
        model = SomeLocationModel
        fields = "__all__"
