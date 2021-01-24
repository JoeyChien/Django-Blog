from django.contrib import admin
from posts.models import Category, Post, CategoryAdmin, PostAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
