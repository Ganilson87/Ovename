from django.db import models
import uuid
from config.settings import AUTH_USER_MODEL
# Produtos

class categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    img = models.ImageField(verbose_name="", upload_to="static/media/img", blank=True)
    nome = models.CharField(verbose_name="Nome", max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "categoria"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.nome

class serie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    img = models.ImageField(verbose_name="", upload_to="static/media/img", blank=True)
    nome = models.CharField(verbose_name="Nome", max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "serie"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.nome
class produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    img1 = models.ImageField(verbose_name="img", upload_to="static/media/img", blank=True)
    img2 = models.ImageField(verbose_name="img", upload_to="static/media/img", blank=True)
    img3 = models.ImageField(verbose_name="img", upload_to="static/media/img", blank=True)
    img4 = models.ImageField(verbose_name="img", upload_to="static/media/img", blank=True)
    nome = models.CharField(verbose_name="Nome", max_length=50)
    descricao = models.TextField(verbose_name="Descrição", max_length=5000000)
    categoria = models.ForeignKey("app.categoria", verbose_name=("categoria"), on_delete=models.CASCADE, related_name='items')
    usuario = models.ForeignKey(AUTH_USER_MODEL,  on_delete=models.CASCADE,  related_name='usuario')
    createdAt = models.DateTimeField(auto_now_add=True)
    preco = models.IntegerField(verbose_name="preco")
    prestacoes = models.IntegerField(verbose_name="prestacoes")
    
    def  image_tag(self):
        return mark_safe('<img src="/../../static/%s" width="150" height="150" />' % (self.img1))

    image_tag.allow_tags = True     
    def __str__(self):
            return ("{}: {} ".format(self.nome, 
        
        self.preco,
        
        ))
    class Meta:
        db_table = "produto"
        ordering = ['-createdAt']

       

    