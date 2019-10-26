from django.db import models
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=100)
    ssn = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = CustomUser.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=CustomUser)
