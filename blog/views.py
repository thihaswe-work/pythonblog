from django.shortcuts import redirect, render ,get_object_or_404
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .forms import CategoryForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def superuser_required(view_func):
    decorated_view_func = user_passes_test(
        lambda u: u.is_superuser
    )(view_func)
    return decorated_view_func

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("user_posts",username=request.user.username)
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
            return redirect("blog/post_detail", slug=slug)
    else:
        form = PostForm(instance=post)
    
    return render(request, "blog/edit_post.html", {"form": form, "post": post})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user == post.author:
        post.delete()

    return redirect("user_posts",username=request.user.username)

@login_required
@superuser_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)
    return render(request, "blog/edit_category.html", {"form": form})

@login_required
@superuser_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    return render(request, "blog/delete_category.html", {"category": category})



#Sessions
from django.http import JsonResponse

def get_count(request):
    count = request.session.get("count", 0)
    return JsonResponse({"count": count})

def increase_count(request):
    count = request.session.get("count", 0)
    count += 1
    request.session["count"] = count
    return JsonResponse({"count": count})

def decrease_count(request):
    count = request.session.get("count", 0)
    count -= 1
    request.session["count"] = count
    return JsonResponse({"count": count})
