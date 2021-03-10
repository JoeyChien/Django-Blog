from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    content = {'posts': posts}
    return render(request, 'index.html', content)

def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save() 
    context = {
        'form' : form
    } 
    return   render(request, "posts/post_create.html", context)