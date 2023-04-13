from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("produtos", produtos, name="produtos"),
    path("produtos/", produtos, name="produtos"),
    path("QuemSomos", about, name="about"),
    path("contact", contact, name="contact"),
    path("produtos/<str:pk>", ProdutoDetail.as_view()),
    
    
    
]
