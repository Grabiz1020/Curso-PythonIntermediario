from django.contrib import admin
from .models import Post
from .models import MyImage
from .models import MyAudio

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "date", "image" , "text", "visible")
    search_fields = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(MyImage)
class PostAdmin(admin.ModelAdmin):
    list_display = ("image","title", "subtitle", "date", "text", "visible")
    search_fields = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(MyAudio)
class PostAdmin(admin.ModelAdmin):
    list_display = ("idnumber","audio", "title", "slug", "text", "visible")
    search_fields = ("idnumber", "title")
    prepopulated_fields = {"slug": ("idnumber",)}