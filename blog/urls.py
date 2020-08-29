from django.urls import path
from .views import (
    HomeView,
    BlogView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    # path("", HomeView.as_view(), name="home"),
    path("", BlogView.as_view(), name="blog"),
    path("post/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    path("post/new/", BlogCreateView.as_view(), name="create_blog"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="update_blog"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="delete_blog"),
]
