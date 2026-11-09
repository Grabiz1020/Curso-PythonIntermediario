from django.contrib import admin
from .models import Post
from .models import MyImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "date", "text", "visible")
    search_fields = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(MyImage)
class PostAdmin(admin.ModelAdmin):
    list_display = ("image","title", "subtitle", "date", "text", "visible")
    search_fields = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}