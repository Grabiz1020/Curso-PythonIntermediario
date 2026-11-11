from django.urls import path
from . import views

app_name = "textposts"

#repare que cada views. tem um nome de uma função
urlpatterns = [
    path("", views.homepage, name="home"),
    path("about/", views.information, name="about"),
    path("art/", views.muralart, name="art"),
    path("text/", views.muralposts, name="textposts"),
    path("text/read/<slug:slug>", views.selectedpost, name="post"),
]