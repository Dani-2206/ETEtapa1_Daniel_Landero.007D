from django.db import models

# Create your models here.
class pais(models.Model):
    idpais = models.IntegerField(primary_key=True,verbose_name='ID del pais')
    pais =models.CharField(max_length=40,verbose_name='Nombre del pais')

    def __str__(self):
        return(self.pais)


class periodista(models.Model):
    rut= models.CharField(max_length=20,primary_key=True,verbose_name='Rut del periodista')
    foto= models.ImageField(upload_to='fotos/', null=True,blank=True)
    nombre_c = models.CharField(max_length=100,verbose_name='Nombre completo')
    telefono = models.IntegerField(verbose_name='Numero de telefono')
    direccion = models.CharField(max_length=90,verbose_name='Direccion')
    email = models.CharField(max_length=50, verbose_name='Email ')
    pais= models.ForeignKey(pais, on_delete=models.CASCADE,verbose_name='Pais')
    contrasena= models.CharField(max_length=50,verbose_name='contraseña')

    def __srt(self):
        return(self.rut)
