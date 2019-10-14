from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
]