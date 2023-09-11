from django.db import models
from accounts.models import UserProfile
class Business(models.Model):
    id_business = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    desc = models.CharField(max_length=100)
    opening_time = models.TimeField(default="07:00:00")
    closing_time = models.TimeField(default="18:00:00")

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    price = models.IntegerField()
    fk_id_business = models.ForeignKey(Business, on_delete=models.CASCADE)

class Request(models.Model):
    id_request = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    status = models.CharField(max_length=30, default="Sin tomar")
    delivery_location = models.CharField(max_length=250)
    desc_delivery = models.CharField(max_length=1000, null=True)
    pick_up_location = models.CharField(max_length=250, default="Pick-up location")
    desc_pick_up_location = models.CharField(max_length=1000, null=True)
    fk_id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fk_id_business = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

