from django.urls import path
from .views import blog_list

urlpatterns = [
    path("lists/",blog_list,name="blog_lists")
]