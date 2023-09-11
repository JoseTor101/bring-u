from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Business,Product, Request
from accounts.models import UserProfile
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
@login_required
def product(request, id_business):
    business = get_object_or_404(Business, pk=id_business)
    products = business.product_set.all()  # Obtener todos los productos asociados al restaurante
    return render(request, 'business_detail.html', {'business': business, 'products': products})

@login_required
def profile(request, id_del=None):
    #revisar esto
    user = request.user
    
    #MOSTRAR ORDENES EN CURSO
    #Buscar como obtener id de usuario de la manear apropiada
    user_requests = Request.objects.filter(fk_id_user=2)
    #print("😀",user_requests)

    context = {
        'user': user,
        'orders': user_requests,
    }
    if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
        product_id = request.POST.get('product_id')
        try:
            delete_order = Request.objects.get(fk_id_product=product_id)
            delete_order.delete()
        except Request.DoesNotExist:
            # Handle the case where the order with the specified product ID does not exist
            pass
        return redirect('/profile')


    #CREACION DE ORDEN

    if request.method == "POST":
        form_data = request.POST
        #print("🐾", form_data)
        user_id = UserProfile.objects.get(id_user=2)
        product = Product.objects.get(id_product=form_data['product_id'])
        business = Business.objects.get(name=form_data['business_name'])
        #print("🐾", form_data)
        
        Request.objects.create(
                fk_id_user=user_id,
                fk_id_business=business,
                fk_id_product=product,
                name=form_data['product_name'],
                desc=form_data['product_desc'],
                price=form_data['product_price'],
                pick_up_location=form_data['business_name'],
                delivery_location=form_data['delivery_location'],
                desc_delivery=form_data['desc_delivery'],
            )

        return redirect('/profile')

    


    return render(request, 'profile.html', context)

def orders(request):
    return render(request, 'request.html')
