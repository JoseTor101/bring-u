from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from bring_u.models import Business, Product
from accounts.models import UserProfile
import json
from .AI import read_image_from_dataUri
# Manejo de imágenes
from django.core.files.uploadedfile import SimpleUploadedFile
# Campo requerido para ver la vista

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def addmenu(request):
    businesses = Business.objects.all()
    context = {'businesses': businesses}
    data = None

    try:
        if request.method == 'POST' and request.POST.get('method') == 'SAVE_PRODUCTS':
            # Accede directamente a los datos del formulario
            selected_business_id = request.POST.get('selected_business_id')
            item_names = request.POST.getlist('item_name[]')
            item_prices = request.POST.getlist('item_price[]')
            item_descs = request.POST.getlist('item_desc[]')

           
            # Realiza las acciones necesarias con los datos del formulario
            if selected_business_id:
                selected_business = Business.objects.get(id_business=selected_business_id)


                for name, price, desc in zip(item_names, item_prices, item_descs):
                    Product.objects.create(
                        fk_id_business=selected_business,
                        name=name,
                        price=price,
                        desc=desc
                    )

                # Puedes agregar mensajes de éxito o redireccionar a otra página.
                messages.success(request, 'Productos guardados exitosamente.')
                return redirect('/addmenu')
            else:
                messages.error(request, 'Seleccione un negocio antes de guardar los productos.')

        if request.method == 'POST':
            cropped_img = request.POST.get('image-data')
            data = read_image_from_dataUri(cropped_img)

        if data:
            items = data.split(';')
            cleaned_items = []

            for item in items:
                if item:
                    item_split = item.split('_')
                    cleaned_items.append(item_split)

            context['data_list'] = cleaned_items

    except Exception as e:
        # Manejar la excepción aquí (puedes imprimir o registrar el error)
        messages.error(request, f'Error en la vista: {str(e)}')
        return redirect("/profile")

    return render(request, 'addmenu.html', context)
