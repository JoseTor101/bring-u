from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Business,Product, Request
from accounts.models import UserProfile
import json
#manejo de imagenes
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your views here.

def home(request):
    return render(request, 'home.html')

def business(request):
    user = request.user

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

    #CREACION DE ORDEN
    if request.method == "POST":
        form_data = request.POST
        user_id = UserProfile.objects.get(id=user.id)
        product = Product.objects.get(id_product=form_data['product_id'])
        business = product.fk_id_business.name
        
        Request.objects.create(
                fk_id_user=user_id,
                fk_id_product=product,
                business_name=business,
                name=form_data['product_name'],
                desc=form_data['product_desc'],
                price=form_data['product_price'],
                pick_up_location=form_data['business_name'],
                delivery_location=form_data['delivery_location'],
                desc_delivery=form_data['desc_delivery'],
            )

        return redirect('/profile')

    return render(request, 'business.html', businessesDict  )
@login_required
def product(request, id_business):
    business = get_object_or_404(Business, pk=id_business)
    products = business.product_set.all()  # Obtener todos los productos asociados al restaurante
    return render(request, 'business_detail.html', {'business': business, 'products': products})

@login_required
def profile(request):
    
    user = request.user
    user_profile = UserProfile.objects.get(username=user)

    #MOSTRAR ORDENES EN CURSO

    user_id = user.id
    user_requests = Request.objects.filter(fk_id_user=user.id)
    
    context = {
        'user': user,
        'orders': user_requests,
    }

    #ELIMINAR ORDEN 

    if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
        order_id = request.POST.get('order_id')  # Retrieve the id_request from the POST data
        try:
            delete_order = Request.objects.get(id_request=order_id)
            delete_order.delete()
        except Request.DoesNotExist:
            pass
        return redirect('/profile') 

    #ENTREGAR PEDIDOS 
    print(request)
    if request.method == 'POST':
        deliver_orders = request.POST.get('deliver-orders')
        #deliver_orders = request.POST
        print(deliver_orders, "💫")
        if not user.is_service_prov and (deliver_orders == 'on'):
            print("Voy a ser", "💙")
            user_profile.is_service_prov = True
            user_profile.save()
            #return redirect("/profile")
        elif user.is_service_prov and not deliver_orders:
            print("Ya no más", "💙")
            user_profile.is_service_prov = False
            user_profile.save()
            #return redirect("/profile")
    
    
    return render(request, 'profile.html', context)

#SELECCIONAR SI QUIERES UNA PETICION PERSONALIZADA O DE RESTAURANTES
def orders(request):
    return render(request, 'request.html')

#CREAR SOLICITUD PERSONALIZADA EN "my_request.html"

def my_request(request):
    user = request.user

    if request.method == "POST":
        form_data = request.POST
        uploaded_file = request.FILES.get('file') 
        user_id = UserProfile.objects.get(id=user.id)

        Request.objects.create(
                fk_id_user=user_id,
                name=form_data['name_order'],
                desc=form_data['desc_order'],
                price=form_data['price'],
                pick_up_location=form_data['pick_up_location'],
                desc_pick_up_location=form_data['desc_pick_up_location'],
                delivery_location=form_data['delivery_location'],
                desc_delivery=form_data['desc_delivery'],
                file=SimpleUploadedFile(uploaded_file.name, uploaded_file.read()) if uploaded_file else None,
            )

        return redirect('/profile')



    return render(request, 'my_request.html')
