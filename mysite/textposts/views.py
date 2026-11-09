from django.shortcuts import render
from .models import MyImage
#from .models import MUDE AQUI O NOME DO POST 

def homepage(request):
    myimages = MyImage.objects.all()
    return render(request, "textposts/home.html", {"myimages": myimages})
