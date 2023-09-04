from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    is_service_prov = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    tel = models.IntegerField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=50, default="123")
    profile_pic = models.BinaryField()
