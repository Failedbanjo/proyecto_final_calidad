from django.db import models
from django.contrib.auth.models import User

class Verificacion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=6)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.codigo}"