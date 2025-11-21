from django.shortcuts import redirect, render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

from django.contrib.auth.decorators import login_required
from .forms import PostForm

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})

def category_list(request):
    categories = Category.objects.all()
    return render(request, "blog/category_list.html", {"categories": categories})
