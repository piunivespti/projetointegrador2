from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import produto
from .forms import ProdutoForm

# Create your views here.
def inicio(request):
    return render(request, "paginas/inicio.html")

def sobre(request):
    return render(request, 'paginas/sobre.html')
 
def produtos(request):
    produtos = produto.objects.all()
    print(produtos)
    return render(request, 'produtos/index.html', {'produtos': produtos})

def criar(request):
    formulario = ProdutoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect ('produtos')
    return render(request, 'produtos/criar.html', {'formulario': formulario})

def editar(request, id):
    prod = produto.objects.get(id=id)
    formulario = ProdutoForm(request.POST or None, request.FILES or None, instance=prod)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('produtos')

    return render(request, 'produtos/editar.html', {'formulario': formulario})

def apagar(request, id):
    prod = produto.objects.get(id=id)
    prod.delete()
    return redirect ('produtos')