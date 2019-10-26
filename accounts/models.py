from django.db import models
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.contrib.auth.base_user import BaseUserManager
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(_('The username must be set'))
        if not email:
            raise ValueError(_('The Email must be set'))
        #username = username
        #user = self.model(email=email, **extra_fields)
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=100)
    ssn = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()
    def __str__(self):
        return self.username

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = CustomUser.objects.create(user=kwargs['instance'])

#post_save.connect(create_profile, sender=CustomUser)
