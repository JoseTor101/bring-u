from django.db import models
from accounts.models import UserProfile
class Business(models.Model):
    id_business = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    desc = models.CharField(max_length=100)
    opening_time = models.TimeField(default="07:00:00")
    closing_time = models.TimeField(default="18:00:00")

    def __str__(self):
        return self.name

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    price = models.IntegerField()
    fk_id_business = models.ForeignKey(Business, on_delete=models.CASCADE)

# Define the upload_to function
def upload_to(instance, filename):
    # Generate a safe file path within the 'orders_media' directory
    return f'media/{filename}'
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
    file= models.FileField(upload_to=upload_to, null=True)
    fk_id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fk_id_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    business_name = models.CharField(max_length=70, null=True)

class Delivery(models.Model):
    id_delivery = models.AutoField(primary_key=True)
    fk_id_request = models.ForeignKey(Request, on_delete=models.CASCADE)
    fk_id_client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_deliveries', default=None)
    fk_id_delivery_man = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='delivery_man_deliveries')
    time = models.TimeField(auto_now=True)
