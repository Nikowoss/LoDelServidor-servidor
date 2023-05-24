from django.db import models

# Create your models here.

REGION = [
        ("RM", "Santiago"),
        ("8", "VIII Bio-BIo"),
        ("9", "IX Araucania"),
    ]
CARGO = [
        ("1", "Encargado ventas"),
        ("2", "Administrador de usuarios"),
        ("3", "Administrador de cuentas"),
        ("4", "Encargado pagina web")
    ]

class Cliente(models.Model):
    rut=models.CharField(primary_key=True, null=False, max_length=12)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    correo=models.CharField(max_length=100)
    contra=models.CharField(max_length=12)
    direccion=models.CharField(max_length=45)
    region=models.CharField(max_length=2,choices=REGION)
    comuna=models.CharField(max_length=40)
    telefono=models.IntegerField()
    
class Administrador(models.Model):
    rut=models.CharField(primary_key=True, null=False, max_length=12)
    nombre=models.CharField(max_length=40)
    correo=models.CharField(max_length=100)
    contra=models.CharField(max_length=12)
    telefono=models.IntegerField()
    cargo=models.CharField(max_length=1,choices=CARGO)


    
class Vinilo(models.Model):
    id=models.AutoField(primary_key=True)
    cara_delante = models.FileField(upload_to="files/%Y/%m/%d")
    cara_detras = models.FileField(upload_to="files/%Y/%m/%d")
    nombre_cantante=models.CharField(max_length=40)
    nombre_vinilo=models.CharField(max_length=40)
    estilo=models.CharField(max_length=40) #Esto se podia dejar como un choise tambien
    precio=models.IntegerField()
    cantidad=models.IntegerField()

class Carrito(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=10)
    producto=models.CharField(max_length=20)
    cantidad=models.IntegerField()