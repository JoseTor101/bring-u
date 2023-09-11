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

    if request.method == "POST":
        form_data = request.POST
        print ("😎",user)
        user_id = User.objects.get(username=user.username)
        
        business = Business.objects.get(name=form_data['business_name'])
        business_id = business.id_business

        Request.objects.create(
                fk_id_user=user_id,
                fk_id_business=business,
                name=form_data['product_name'],
                desc=form_data['product_desc'],
                price=form_data['product_price'],
                pick_up_location=form_data['business_name'],
                delivery_location=form_data['delivery_location'],
                desc_delivery=form_data['desc_delivery'],
            )

        return redirect('/')

        """for field_name, field_value in form_data.items():
            print(f"Field Name: {field_name}, Field Value: {field_value}")"""


    return render(request, 'profile.html', context)

def orders(request):
    return render(request, 'request.html')
