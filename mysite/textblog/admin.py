from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "splash_image", "release_date")
    search_fields = ("title", "subtitle", "release_date")
    list_filter = ("title",)
    prepopulated_fields = {"slug": ("titulo",)}