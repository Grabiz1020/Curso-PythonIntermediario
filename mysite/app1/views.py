from django.shortcuts import get_object_or_404, render
#Antes só estava aqui o render. Não estava o get_object_or_404

from .models import Livro 
#Isso você faz para pegar o obj livro

def lista_livro(request):
    livros = Livro.objects.all()
    return render(request, "app1/lista_livro.html", {"livros": livros})

def comprar_livro(request, slug):
    livro = get_object_or_404(Livro)
    return render(request, "app1/lista_livros.html", {"livros": livro})