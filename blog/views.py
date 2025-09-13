from django.shortcuts import render
from .models import Blog, Category

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()

    categories = Category.objects.all()

    context = {
        "blogs": blogs,
        "categories": categories
    }

    return render(request,'blogs/blogs.html',context)
