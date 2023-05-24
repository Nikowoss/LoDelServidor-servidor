from django.contrib import admin
from .models import Cliente, Administrador, Vinilo, Carrito

# Register your models here.

class admCliente(admin.ModelAdmin):
    list_display=["rut","nombre","apellido","correo","contra","direccion","region","comuna","telefono"]
    
    class meta:
        model=Cliente

class admAdministrador(admin.ModelAdmin):
    list_display=["rut","nombre","correo","contra","telefono","cargo"]
    list_editable=["nombre","correo","contra","telefono","cargo"]
    
    class meta:
        model=Administrador

class admVinilo(admin.ModelAdmin):
    list_display=["id","cara_delante","cara_detras","nombre_cantante","nombre_vinilo","estilo","precio","cantidad"]
    list_editable=["cara_delante","cara_detras","nombre_cantante","nombre_vinilo","estilo","precio","cantidad"]

    class meta:
        model=Vinilo

class admCarrito(admin.ModelAdmin):
    list_display=["id","user","producto","cantidad"]

    class meta:
        model=Carrito

admin.site.register(Cliente,admCliente)
admin.site.register(Administrador,admAdministrador)
admin.site.register(Vinilo,admVinilo)
admin.site.register(Carrito,admCarrito)
