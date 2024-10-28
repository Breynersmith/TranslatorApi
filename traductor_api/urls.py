# urls.py (en el proyecto principal, no en la aplicación)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # tus rutas aquí
    path('api/', include('traductorApp.urls')),  # Ajusta esta línea a tu aplicación
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
