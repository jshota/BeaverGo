from django.test import TestCase
from model import CustomUser
# Create your tests here.
"""class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(name="lion", sound="roar")
        CustomUser.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = CustomUser.objects.get(name="lion")
        cat = CustomUser.objects.get(name="cat")
        #self.assertEqual(lion.speak(), 'The lion says "roar"')
        #self.assertEqual(cat.speak(), 'The cat says "meow"')
        """
