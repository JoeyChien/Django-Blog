from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    content = {'posts': posts}
    return render(request, 'index.html', content)
    