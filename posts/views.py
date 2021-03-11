from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    content = {
        'posts': posts
    }
    return render(request, 'index.html', content)

def singlePost(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)

def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save() 
        form = PostForm()
    context = {
        'form': form
    } 
    return render(request, "posts/post_create.html", context)

