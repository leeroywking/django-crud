## Django Models

Lab28-Django CRUD
*Author: Lee-Roy King*

----

## Description
This application is a simple Django server with a "blog" model that can be viewed at /blog as well as CRUD methods for those blog articles

---

### Getting Started
Clone this repository to your local machine.

```
$ git clone git@github.com:leeroywking/django-crud.git
```

### To run the program 
```
cd django-models
poetry install
poetry shell
django-admin runserver
```

---

### Routes
path("", BlogView.as_view(), name="blog"),
path("post/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
path("post/new/", BlogCreateView.as_view(), name="create_blog"),
path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="update_blog"),
path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="delete_blog"),
---

### Change Log
1.0 feature complete


------------------------------
