from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def profile_view(request):
    profile = CustomUserCreationForm.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    template = 'accounts/profile.html'
    return render(request, template, context)
