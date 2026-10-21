from django.contrib import admin

from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "preco", "estilo_capa")
    search_fields = ("titulo", "autor")
    list_filter = ("estilo_capa",)
    prepopulated_fields = {"slug": ("titulo",)}