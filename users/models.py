from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    bi = models.CharField(max_length=15, unique=True)
    foto = models.ImageField(verbose_name="", upload_to="static/media/img", blank=True)
    nivel_choices = [
        ('Tecnico de Manutençao','tec'),
        ('CEO','ceo'),
        ('Funcionario','funcionario')
    ]
    Telefone = models.CharField(max_length=14, unique=True)
    Nivel = models.CharField(choices= nivel_choices , max_length=50)
    verificado = models.BooleanField(default=False)
    
      