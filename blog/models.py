from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)  # o ForeignKey a un modelo de usuario
    fecha = models.DateField(auto_now_add=True)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to='blog_images/', blank=True, null=True)