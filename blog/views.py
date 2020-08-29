from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Blog
from django.urls import reverse

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class BlogView(ListView):
    template_name = "blog.html"
    model = Blog


class BlogDetailView(DetailView):
    template_name = "blog_detail.html"
    model = Blog


class BlogCreateView(CreateView):
    template_name = "create_blog.html"
    model = Blog
    fields = "__all__"


class BlogUpdateView(UpdateView):
    template_name = "update_blog.html"
    model = Blog
    fields = "__all__"


class BlogDeleteView(DeleteView):
    template_name = "delete_blog.html"
    model = Blog

    def get_success_url(self):
        return reverse("blog")
