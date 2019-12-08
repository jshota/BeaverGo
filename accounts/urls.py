from django.urls import path
from django.conf.urls import url
from . import views
#from dlf_app import PlaceCreateView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^profile/$', views.profile_view, name='profile_view'),
    url(r'^new_trips/$',views.new_trips.as_view(), name='new_trips'),
    url(r'^password/$', views.PasswordChangeView.as_view(), name='change'),
    url(r'^test_location/$', views.test_location, name='test_location'),
    url(r'^edit_profile/$', views.Edit_Profile, name='edit_profile'),
]
