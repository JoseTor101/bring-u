from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from bring_u import views as bringuViews 

urlpatterns = [
    path('', bringuViews.home),
    path('admin/', admin.site.urls),
    path('profile/', bringuViews.profile, name='profile'),
    path('request/', bringuViews.orders),
    path('delivery_custom/', bringuViews.delivery_custom),
    path('business/', bringuViews.business, name='business'),
    path('business/<int:id_business>/', bringuViews.product, name='business_detail'),
    path('available_orders/', bringuViews.available_orders),
    path('about_us/', bringuViews.about_us),
    path('accounts/', include('accounts.urls')),
    path('addmenu/', include('AI.urls')),
    path('chat/', include('chat.urls')),
    path('', include('notifications.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)