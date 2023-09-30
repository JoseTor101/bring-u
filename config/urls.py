from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from bring_u import views as bringuViews 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bringuViews.home),
    path('business',bringuViews.business),
    path('business/<int:id_business>/', bringuViews.product, name='business_detail'),
    path('profile', bringuViews.profile),
    path('request', bringuViews.orders),
    path('my_request', bringuViews.my_request),
    path('available_orders', bringuViews.available_orders),
    path('accounts/', include('accounts.urls')),
    path('chat/', include('chat.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)