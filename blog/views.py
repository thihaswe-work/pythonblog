from django.shortcuts import redirect, render ,get_object_or_404

# Create your views here.

from .models import Post, Category
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .forms import CategoryForm

@login_required
def create_post(request):
    print(request,'request is')
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


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")  # redirect to the category list page
    else:
        form = CategoryForm()
    
    return render(request, "blog/create_category.html", {"form": form})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {
        "post": post
    })

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if post.author != request.user:
        return redirect("blog/post_detail", slug=slug)  # only author can edit
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", slug=slug)
    else:
        form = PostForm(instance=post)
    
    return render(request, "edit_post.html", {"form": form, "post": post})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.author:
        post.delete()
    return redirect("user_posts")