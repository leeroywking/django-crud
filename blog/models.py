from django.db import models
from django.urls import reverse

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey("auth.user", default=1, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog")
