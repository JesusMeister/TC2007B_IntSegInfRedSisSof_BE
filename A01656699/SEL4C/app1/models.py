from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.TextField()
    genero = models.TextField()
    edad = models.IntegerField()
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    class Meta:
        app_label = 'app1'