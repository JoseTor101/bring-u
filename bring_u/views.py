from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse

from .models import Business,Product
# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def business(request):
    return render("<h1>Hola</h1>")

def product(request):
    return render("<h1>Hola</h1>")

"""def home(request):
    return render(request, 'home.html')

def restaurants(request):
    searchRestaurant= request.GET.get('searchRestaurant')
    if searchRestaurant:
        restaurants = Restaurants.objects.filter(name__icontains = searchRestaurant)
    else:
        restaurants=  Restaurants.objects.all()
        searchRestaurant = "" 
    restaurantDict = {'restaurants': restaurants,'searchRestaurant':searchRestaurant} 
    return render(request, 'restaurants.html', restaurantDict  )

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurants, pk=restaurant_id)
    menu_items = restaurant.menu_set.all()  # Obtener todos los platos asociados al restaurante
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'menu_items': menu_items})
"""