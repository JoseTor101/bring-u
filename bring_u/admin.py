from django.contrib import admin
from .models import Business
from .models import Product
from .models import Request
from .models import Delivery

# Register your models here.
admin.site.register(Business)
admin.site.register(Product)
admin.site.register(Request)
admin.site.register(Delivery)