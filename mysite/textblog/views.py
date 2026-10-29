from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "textblog/base.html", {"posts":posts})

def post_show(request, slug):
    post = get_object_or_404(Post)
    return render(request, "textblog/base.html", {"posts":posts})