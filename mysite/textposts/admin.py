from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "date", "text")
    search_fields = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}