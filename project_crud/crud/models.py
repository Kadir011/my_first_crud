from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, blank=False, null=False, verbose_name='Código') 
    titulo = models.CharField(max_length=100, blank=False, null=True, verbose_name='Título') 
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imágen') 
    descripcion = models.TextField(blank=False, null=True, verbose_name='Descripción') 

    def __str__(self):
        dato = "Título: " + self.titulo 
        return dato 
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)  
        super().delete() 
    
    class Meta:
        db_table = 'Libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros' 







