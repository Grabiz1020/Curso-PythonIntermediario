from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    splash_image = models.URLField(
            "URL of the splash image",
            max_length=500,
            blank=True,
            help_text=(
                "Give the direct link of an image"
                "to show up. You can leave it blank"
            ),
    )
    release_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["release_date"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("textblog:post_detail", args=[self.slug])
