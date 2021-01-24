from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    output = '</br>'.join([p.title for p in posts])
    return HttpResponse(output)
