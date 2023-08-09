from django.contrib import admin
from .models import Restaurants
from .models import Menu

# Register your models here.
admin.site.register(Restaurants)
admin.site.register(Menu)