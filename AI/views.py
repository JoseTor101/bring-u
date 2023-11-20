from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from bring_u.models import Business,Product
from accounts.models import UserProfile
import json
from .ai import read_image_from_dataUri
#manejo de imagenes
from django.core.files.uploadedfile import SimpleUploadedFile
#Campo requerido para ver la vista

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def addmenu(request):

    businesses = Business.objects.all()
    context = {
        'businesses': businesses
    } 


    if request.method == 'POST':
        cropped_img = request.POST.get('image-data')
        data = read_image_from_dataUri(cropped_img)

        if data:
            items = data.split(';')
            print("😁",data)
            print("😋", items)
            # Split each item into fields based on underscore (_)
            """data_list = []
            for item in items:
                if item:
                    item_split = item.split('_')
                    data_list.append({
                        'nombre': item_split[0],
                        'precio': item_split[1],
                        'descripcion': item_split[2] if len(item_split) > 2 else ''
                    })"""

            context = {
                'data_list': items,
                'businesses': businesses
            }


    return render(request, 'addmenu.html', context)