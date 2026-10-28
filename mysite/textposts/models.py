from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField("title",max_length=90)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField("subtitle",max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    class Meta:
        ordering = ["titulo"]
        verbose_name = "livro"
        verbose_name_plural = "livros"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("catalogo:comprar", args=[self.slug])
    class Meta:
        ordering = ["-date"] # The "-" is to display the newer one to the oldest one.
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("reader:read", args=[self.slug])


# Create your models here.
