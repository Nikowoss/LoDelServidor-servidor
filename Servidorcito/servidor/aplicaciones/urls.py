from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, otrawea, vinilos, añadir, modificarvinilo

#URLS.py aplicaciones
urlpatterns = [
    path('',index,name='index'),
    path('otrawea',otrawea,name='otrawea'),
    path('vinilos',vinilos,name='vinilos'),
    path('añadir',añadir,name='añadir'),
    path('modificarvinilo/<id>',modificarvinilo,name="modificarvinilo"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)