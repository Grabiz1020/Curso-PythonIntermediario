from django.shortcuts import get_object_or_404, render
from .models import MyImage
from .models import Post
#from .models import MUDE AQUI O NOME DO POST 

def homepage(request):
    return render(request, "textposts/home.html")

def information(request):
    return render(request, "textposts/information.html")

def muralart(request):
    myimages = MyImage.objects.all()
    return render(request, "textposts/muralart.html", {"myimages": myimages})

def muralposts(request):
    posts = Post.objects.all()
    return render(request, "textposts/muralposts.html", {"posts": posts})

def selectedpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "textposts\selectedpost", {"post": post})

