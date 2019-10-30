from django.test import TestCase, Client
from django.urls import resolve, reverse
from accounts.views import SignUp, profile_view
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

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.profile_url = reverse('profile_view')
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
    def test_signup_signin(self):
        test_user = CustomUser.objects.get(username = 'Jane Test')
        self.assertEquals(test_user.gender, 'Male')
        self.assertEquals(test_user.address, 'fdsafds')
        self.assertEquals(test_user.ssn, '123456')
        self.assertEquals(test_user.email, 'test@test.com')
