from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .forms import CustomUserCreationForm,LocationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
#from BeaverGo.settings import API_KEY
from .models import CustomUser
from django.contrib.auth import get_user_model,views as auth_view
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def profile_view(request):
    title = "Provider Signup Page"
    home = "BeaverGo"
    return render(request, 'accounts/profile.html', {'title': title, 'home': home})

class new_trips(CreateView):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    title="trip"
    home="BeaverGo"
    form_class = LocationForm
    template_name = 'new_trips.html'
    #return render(request, 'new_trips.html', {'title': title, 'home': home})
class PasswordChangeView(auth_view.PasswordChangeView):
	success_url = reverse_lazy('login')
	template_name = 'registration/change_password.html'
