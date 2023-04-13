from django.shortcuts import render
from .models import *
# Create your views here.
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView


def index(request):
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
 
        
    produtos = produto.objects.all()    
    paginator = Paginator(produtos,3)

    pagina = request.GET.get('pagina')
    produtoall = paginator.get_page(pagina)

    context = {
        'num_visits': num_visits,
        'produtos':produtoall
    
    }
    
    #Paginas
    
    return render(request,"index.html", context=context)
def produtos(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    produtos = produto.objects.all()    
    
    paginator = Paginator(produtos,6)

    pagina = request.GET.get('pagina')
    produtoall = paginator.get_page(pagina)
    categorias = categoria.objects.all()
    cat = request.GET.get('categoria')
    if cat != '' and cat is not None:
        produtosall = produto.objects.filter(categoria=cat)
    
    context = {
        'num_visits': num_visits,
        'produtos':produtoall,
        'categorias':categorias,
    
    }
    
    #Paginas
    return render(request, "produtos.html",context=context)
class ProdutoDetail(DetailView):
    model = produto
    template_name = "ProdutoDetail.html"
def about(request):
    
    return render(request, "about.html")

def contact(request):
    
    return render(request, "contact.html")
    