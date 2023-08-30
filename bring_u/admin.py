from django.contrib import admin
from .models import Business
from .models import Product

# Register your models here.
admin.site.register(Business)
admin.site.register(Product)