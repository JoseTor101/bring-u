from django.db import models
from django.contrib.auth.models import AbstractUser

def upload_to(instance, filename):
    # Generate a safe file path within the 'orders_media' directory
    return f'profile_pics/{instance.username}/{filename}'

class UserProfile(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_service_prov = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=15, unique=True)
    tel = models.IntegerField(null=True)
    profile_pic = models.ImageField(upload_to=upload_to, blank=True, null=True)
    email = models.EmailField()
    pass

