from django.shortcuts import render,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Business,Product, User, Request
import json

# Create your views here.

def home(request):
    return render(request, 'home.html')

def business(request):
    searchBusiness= request.GET.get('searchBusiness')
    if searchBusiness:
        businesses = Business.objects.filter(name__icontains = searchBusiness)
    else:
        businesses =  Business.objects.all()
        searchBusiness = "" 

    
    businessesDict = {
        'businesses': businesses,
        'searchRestaurant':searchBusiness
    } 

    if request.method == "POST":
        print("\n😂 ............. .HELP \n")
        
        form_data = request.POST

        # You can iterate over the form_data dictionary to access individual field values
        for field_name, field_value in form_data.items():
            print(f"Field Name: {field_name}, Field Value: {field_value}")

        # Your proc
    return render(request, 'business.html', businessesDict  )

def product(request, id_business):
    business = get_object_or_404(Business, pk=id_business)
    products = business.product_set.all()  # Obtener todos los productos asociados al restaurante
    return render(request, 'business_detail.html', {'business': business, 'products': products})

@login_required
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

def orders(request):
    return render(request, 'request.html')
