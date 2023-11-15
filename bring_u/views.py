from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Business,Product, Request, Delivery
from chat.models import Chat
from accounts.models import UserProfile
import json
from AI.AI import read_image_from_dataUri
#manejo de imagenes
from django.core.files.uploadedfile import SimpleUploadedFile
#Campo requerido para ver la vista
from .decorators import is_service_prov_required
from notifications.models import Notification


# Create your views here.
def home(request):
    user = request.user
    unread_notifications = Notification.objects.filter(is_read=False)
    is_delivering = UserProfile.objects.filter(username=user, is_service_prov=True).exists() if user.is_authenticated else False
    
    context = {
        'is_delivering': is_delivering,
        'user':user,
        'unread_notifications': unread_notifications,
    }
    return render(request, 'home.html', context)

@login_required
def business(request):
    try: 
        user = request.user
        is_delivering = UserProfile.objects.filter(username=user, is_service_prov=True).exists() if user.is_authenticated else False

        searchBusiness= request.GET.get('searchBusiness')
        if searchBusiness:
            businesses = Business.objects.filter(name__icontains = searchBusiness)
        else:
            businesses =  Business.objects.all()
            searchBusiness = "" 

        
        businessesDict = {
            'businesses': businesses,
            'searchRestaurant':searchBusiness,
            'is_delivering':is_delivering
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
    except:
        return redirect('/not_found')

@login_required
def product(request, id_business):
    business = get_object_or_404(Business, pk=id_business)
    products = business.product_set.all()  # Obtener todos los productos asociados al restaurante
    return render(request, 'business_detail.html', {'business': business, 'products': products})

@login_required
def profile(request):
    
    user = request.user
    user_profile = UserProfile.objects.get(username=user)
    is_delivering = UserProfile.objects.filter(username=user, is_service_prov=True).exists() if user.is_authenticated else False
    deliveries = Delivery.objects.filter(fk_id_delivery_man=user_profile.id).exclude(finished=True)

    #MOSTRAR ORDENES EN CURSO

    user_id = user.id
    user_requests = Request.objects.filter(fk_id_user=user.id).exclude(status="Finalizado")
    
    context = {
        'user': user,
        'orders': user_requests,
        'is_delivering': is_delivering,
        'deliveries':deliveries
    }

    #ELIMINAR ORDEN 

    if request.method == 'POST' and request.POST.get('_method') == 'DELETE_ORDER':
        order_id = request.POST.get('order_id')  
        try:
            delete_order = Request.objects.get(id_request=order_id)
            delete_order.delete()
        except Request.DoesNotExist:
            pass
        return redirect('/profile') 

    #CANCELAR ENTREGA

    if request.method == 'POST' and request.POST.get('_delivery') == 'DELETE_DELIVERY':
        delivery_id = request.POST.get('delivery_id')  
        try:
            delete_order = Delivery.objects.get(id_delivery=delivery_id)
            order_untake = Request.objects.get(id_request=delete_order.fk_id_request.id_request)
            order_untake.status = "Sin tomar"
            order_untake.save()
            delete_order.delete()
        except Request.DoesNotExist:
            pass
        return redirect('/profile') 

    #FINALIZAR ENTREGA

    if request.method == 'POST' and request.POST.get('_delivery') == 'FINISH_DELIVERY':

        delivery_id = request.POST.get('delivery_id')  
        delivery_object = Delivery.objects.get(id_delivery=delivery_id)
        request_item = Request.objects.get(id_request=delivery_object.fk_id_request.id_request)

        Notification.objects.create(
            recipient=request_item.fk_id_user,
            message="Confirma la finalización de tu última entrega en el apartado de PERFIL (PROFILE)",
        )

        return redirect('/profile') 

    #ORDEN RECIBIDA

    if request.method == 'POST' and request.POST.get('_method') == 'RECEIVED_ORDER':

        order_id = request.POST.get('order_id')  
        order_object = Request.objects.get(id_request=order_id)

        order_object.status = "Finalizado"
        order_object.save()

        delivery_associated = Delivery.objects.get(fk_id_request=order_id)
        delivery_associated.finished = True
        delivery_associated.save()

        return redirect('/profile') 

    #ENTREGAR PEDIDOS 
    print(request)
    if request.method == 'POST':
        deliver_orders = request.POST.get('deliver-orders')
        if not user.is_service_prov and (deliver_orders == 'on'):
            user_profile.is_service_prov = True
            user_profile.save()
            return redirect("/available_orders")
        elif user.is_service_prov and not deliver_orders:
            user_profile.is_service_prov = False
            user_profile.save()
            return redirect("/profile")
    
    
    return render(request, 'profile.html', context)

@login_required
#SELECCIONAR SI QUIERES UNA PETICION PERSONALIZADA O DE RESTAURANTES
def orders(request):
    user = request.user
    is_delivering = UserProfile.objects.filter(username=user, is_service_prov=True).exists() if user.is_authenticated else False
    context = {
        'is_delivering':is_delivering
    }
    return render(request, 'request.html', context)

#CREAR SOLICITUD PERSONALIZADA EN "my_request.html"
@login_required
def my_request(request):
    user = request.user
    is_delivering = UserProfile.objects.filter(username=user, is_service_prov=True).exists() if user.is_authenticated else False

    context = {
        'is_delivering':is_delivering
    }
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

        return redirect('/profile', context)



    return render(request, 'my_request.html', context)

#VER ÓRDENES QUE SE PUEDEN TOMAR EN "available_orders.html"
@login_required
@is_service_prov_required
def available_orders(request):
    user= request.user
    is_delivering = UserProfile.objects.filter(username=user, is_service_prov=True).exists() if user.is_authenticated else False
    #user_requests = Request.objects.all()
    user_requests = Request.objects.exclude(status="Tomado").exclude(status="Finalizado")

    context = {
        'is_delivering':is_delivering,
        'user_request':user_requests
    }

    #Tomar ordenes 
    if request.method == "POST":
            # Check if the user already has an ongoing delivery
            try:
                current_delivery = Delivery.objects.filter(fk_id_delivery_man=user).latest('time')
                deliver_ongoing = current_delivery.finished
                
                print("DELIVER: ", deliver_ongoing)
                if deliver_ongoing == False:
                    return redirect('/')
                else:
                    order_id = request.POST.get('order_id')  
                    order = Request.objects.get(id_request=order_id)

                    delivery_exists = Delivery.objects.filter(fk_id_request=order_id).first()

                    if not delivery_exists:
                        user_id = UserProfile.objects.get(username=user).id
                        fk_client = UserProfile.objects.get(username=order.fk_id_user)

                        delivery = Delivery.objects.create(
                            fk_id_request=order,
                            fk_id_client = fk_client,
                            fk_id_delivery_man = user,
                        )
                        order.status = "Tomado"
                        order.save()

                        Chat.objects.create(
                            fk_id_delivery=delivery,
                        )
                        return redirect('/profile')
                    else:
                        print('Orden ya tomada')
                        return redirect('/')

            except :
                return redirect('/')

    return render(request, "available_orders.html", context)

@login_required
def addmenu(request):
    if request.method == 'POST':
        cropped_img = request.POST.get('image-data')
        read_image_from_dataUri(cropped_img)
    return render(request, 'addmenu.html')

def about_us(request):
    return render(request, 'about_us.html')
