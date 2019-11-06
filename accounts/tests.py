from django.test import TestCase, Client
from django.urls import resolve, reverse
from accounts.views import SignUp, profile_view
from accounts.models import CustomUser
import json

class TestUrls(TestCase):
    def test_signup_url_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class, SignUp)
    
    def test_profile_url_resolved(self):
        url = reverse('profile_view')
        self.assertEquals(resolve(url).func, profile_view)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.profile_url = reverse('profile_view')

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_profile_input(self):

        response = self.client.post(self.profile_url, {
            'username': 'test',
            'email': 'test@test.com',
            'password': '^ERTET122#@$'
        })

        self.assertEquals(response.status_code, 200)
