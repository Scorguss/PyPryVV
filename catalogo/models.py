from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EBook(models.Model):
    ESTADOS = [
        ('Borrador', 'Borrador'),
        ('Publicado', 'Publicado'),
    ]

    titulo = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    autor_nombre = models.CharField(max_length=100, blank=True) # Nombre visible del autor
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ebooks', null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Borrador')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Capitulo(models.Model):
    ebook = models.ForeignKey(EBook, on_delete=models.CASCADE, related_name='capitulos')
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    orden = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.ebook.titulo} - {self.titulo}"