from django.urls import path
from . import views

app_name = "textposts"

#repare que cada views. tem um nome de uma função
urlpatterns = [
    path("", views.homepage, name="home"),
]