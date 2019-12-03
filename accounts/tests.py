from django.test import TestCase, Client
from django.urls import resolve, reverse
from accounts.views import SignUp, profile_view, new_trips, PasswordChangeView, Edit_Profile
from accounts.models import CustomUser
import json

class TestUrls(TestCase):
    # Sign-up URL test
    def test_signup_url_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class, SignUp)
    
    # Profile URL test
    def test_profile_url_resolved(self):
        url = reverse('profile_view')
        self.assertEquals(resolve(url).func, profile_view)

    # Map URL test
    def test_map_url_resolved(self):
        url = reverse('new_trips')
        self.assertEquals(resolve(url).func.view_class, new_trips)

    # Password Reset URL test
    def test_pwreset_url_resolved(self):
        url = reverse('change')
        self.assertEquals(resolve(url).func.view_class, PasswordChangeView)

    # Edit Profile URL test
    def test_edit_profile_url_resolved(self):
        url = reverse('edit_profile')
        self.assertEquals(resolve(url).func, Edit_Profile)

    # Select Car URL test
    def test_select_car_url_resolved(self):
        url = reverse('select_car')
        self.assertEquals(resolve(url).func, Select_Car)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.profile_url = reverse('profile_view')
        self.map_url = reverse('new_trips')
        self.resetpw_url = reverse('change')
        self.edit_profile_url = reverse('edit_profile')
        self.select_car_url = reverse('select_car')
        CustomUser.objects.create_user(
            username = 'Jane Test',
            password = '23sdaf235@',
            gender = 'Male',
            address = 'fdsafds',
            ssn = '123456', 
            email = 'test@test.com')

    # Sign-up UI test
    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    # User-Profile UI test
    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    # Sign-up test
    def test_signup(self):
        test_user = CustomUser.objects.get(username = 'Jane Test')
        self.assertEquals(test_user.gender, 'Male')
        self.assertEquals(test_user.address, 'fdsafds')
        self.assertEquals(test_user.ssn, '123456')
        self.assertEquals(test_user.email, 'test@test.com')

    # Map UI test
    def test_Map_GET(self):
        response = self.client.get(self.map_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_trips.html')

    # Edit profile UI test
    def test_edit_profile_GET(self):
        response = self.client.get(self.edit_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_profile.html')

    # Select car UI test
    def test_select_car_GET(self):
        response = self.client.get(self.select_car_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'select_car.html')

    # Change Password test
    def test_changepw_GET(self):
        response = self.client.get(self.resetpw_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'change_password.html')
