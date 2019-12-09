from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse
from .forms import CustomUserCreationForm, LocationForm, CustomUserChangeForm, DateForm, CarModel
from django.contrib.auth.decorators import login_required
from django import forms
from .models import CustomUser, SomeLocationModel
from django.contrib.auth import get_user_model, views as auth_view

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def Edit_Profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile_view'))
    else:
        form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

def profile_view(request):
    title = "Provider Signup Page"
    home = "BeaverGo"
    return render(request, 'accounts/profile.html', {'title': title, 'home': home})

class new_trips(CreateView):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    title = "trip"
    home = "BeaverGo"
    form_class = LocationForm
    success_url = reverse_lazy('date_select')
    template_name = 'new_trips.html'
    #return render(request, 'new_trips.html', {'title': title, 'home': home})

class PasswordChangeView(auth_view.PasswordChangeView):
	success_url = reverse_lazy('login')
	template_name = 'registration/change_password.html'

def test_location(request):
    title = 'test'
    home = "BeaverGo"
    #model = SomeLocationModel.objects.all()
    content = SomeLocationModel.objects.values_list('address', flat=True).distinct()
    #address = content 
    #form = MyModelForm(instance=model)
    return render(request, 'test_location.html', {'content': content})

def Date(request):
    title = "Date"
    home = "BeaverGo"
    form = DateForm
    template_name = 'Date.html'
    return render(request, 'Date.html', {'title': title, 'form': form})

def date_select(request):
    title = "Date"
    home = "BeaverGo"
    if request.method == 'POST':
        reservation_time = request.POST['reservation_time']
        reservation_time = reservation_time.split('T')
        date = reservation_time[0]
        time = reservation_time[1]
        carModel = request.POST.get('carModel')
        # time.append(carModel)
        return render(request, 'time_result.html', {'title': title, 'date': date, 'time': time, 'carModel': carModel})
    else:
        #args = {'form': form}
        return render(request, 'date_select.html')

def model_select(request):
    title = "Date"
    home = "BeaverGo"
    template_name = 'model_select.html'
    return render(request, 'test_location.html', {'title': title, 'form': form})
