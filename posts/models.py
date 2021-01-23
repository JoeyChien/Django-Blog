from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 20)
    create_time = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='post')
    create_time = models.DateTimeField(auto_now_add=True)
