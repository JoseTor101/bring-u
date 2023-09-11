from django.db import models
from django.contrib.auth.models import AbstractUser
class UserProfile(AbstractUser):
    id = models.AutoField(primary_key=True)
    is_service_prov = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tel = models.IntegerField(null=True)
    profile_pic = models.ImageField(upload_to='media/users', blank=True, null=True)
    #email = models.CharField(max_length=60)
    pass