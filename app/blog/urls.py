from django.urls import include, path
from django.http import HttpResponse


def blog_view(request, blog_id = 0):
    html = f"<html><body>You blog id is {blog.id}.</body>.</html>"

urlpatterns = [
    path('<int:blog_id>', blog_view)
]