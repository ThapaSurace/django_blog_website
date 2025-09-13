from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by("-created_at")[:4]
    context = {
        "blogs" : blogs
    }
    return render(request,'home/home.html',context)


def about(request):
    return render(request,'about/about.html')