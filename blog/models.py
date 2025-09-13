from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Blog(models.Model):
    name = models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="blogs")
    content = models.TextField()
    author = models.CharField(max_length=100)
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} by {self.author}"
