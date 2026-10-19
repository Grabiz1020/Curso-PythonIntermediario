from django.urls import path
from . import views

app_name = "app1"

#repare que cada views. tem um nome de uma função
urlpatterns = [
    path("", views.lista_livro, name="lista"),
    path("comprar/<slug:slug>", views.comprar_livro, name="listaa"),
]