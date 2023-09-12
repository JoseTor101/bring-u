from django.contrib import admin
from .models import Business
from .models import Product
from .models import Request

# Register your models here.
admin.site.register(Business)
admin.site.register(Product)
admin.site.register(Request)