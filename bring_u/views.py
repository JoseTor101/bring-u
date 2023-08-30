from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse

from .models import Business,Product
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
    businessesDict = {'businesses': businesses,'searchRestaurant':searchBusiness} 
    return render(request, 'business.html', businessesDict  )

def product(request, id_business):
    business = get_object_or_404(Business, pk=id_business)
    products = business.product_set.all()  # Obtener todos los productos asociados al restaurante
    return render(request, 'business_detail.html', {'business': business, 'products': products})
