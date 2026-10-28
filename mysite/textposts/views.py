from django.shortcuts import render

#from .models import MUDE AQUI O NOME DO POST 

def homepage(request):
    return render(request, "textposts/home.html")
