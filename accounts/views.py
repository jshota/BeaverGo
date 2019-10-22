from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth import get_user_model
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def profile_view(request):
    title = "Provider Signup Page"
    home = "BeaverGo"
    return render(request, 'accounts/profile.html', {'title': title, 'home': home})
