from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, SomeLocationModel
from mapbox_location_field.spatial.forms import SpatialLocationField
from bootstrap_datepicker_plus import DateTimePickerInput


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'ssn', 'first_name',
                  'last_name', 'address', 'phone', 'gender', 'image')


class CustomUserChangeForm(UserChangeForm):

    class Meta():
        model = CustomUser
        fields = ('username', 'email', 'phone', 'gender')


class LocationForm(forms.ModelForm):
    class Meta:
        model = SomeLocationModel
        fields = "__all__"


class DateForm(forms.Form):
    model = SomeLocationModel
    fields = ['start_datetime']
    widgets = {
        'start_datetime': DateTimePickerInput()
    }

class CarModel(forms.Form):
    model = SomeLocationModel
    fields = ('car_model')
