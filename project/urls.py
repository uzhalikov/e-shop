from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('baseadmin/', admin.site.urls),
    path('', include('app.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', include('adm.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)