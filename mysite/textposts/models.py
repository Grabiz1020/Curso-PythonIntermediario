from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField("title",max_length=90)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField("subtitle",max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'images/textbanners/', blank=True, null=True,)

    class Meta:
        ordering = ["-date"] # The "-" is to display the newer one to the oldest one.
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("reader:read", args=[self.slug])



class MyImage(models.Model):
    image = models.ImageField(upload_to = 'images/art/')
    title = models.CharField("title",max_length=90)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField("subtitle",max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date"] # The "-" is to display the newer one to the oldest one.
        verbose_name = "myimage"
        verbose_name_plural = "myimages"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("reader:read", args=[self.slug])


class MyAudio(models.Model):
    idnumber = models.FloatField("idnumber",max_length=90)
    audio = models.FileField(upload_to = 'audio/modelaudio/')
    title = models.CharField("title",max_length=90)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["idnumber"] # The "-" is to display the newer one to the oldest one.
        verbose_name = "myaudio"
        verbose_name_plural = "myaudios"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("reader:read", args=[self.slug])

# Create your models here.
