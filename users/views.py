from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import os

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")  # name of your post list URL
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

def user_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()  # uses related_name in Post model
    return render(request, "users/user_posts.html", {"user": user, "posts": posts})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("post_list")  # redirect after login
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("post_list")

@login_required
def edit_profile(request):
    profile = request.user.profile  # get current user's profile

    if request.method == "POST":
        bio = request.POST.get("bio", "")
        avatar = request.FILES.get("avatar")

        profile.bio = bio
        if avatar:
             if profile.avatar:
                old_avatar_path = profile.avatar.path
                if os.path.isfile(old_avatar_path):
                    os.remove(old_avatar_path)
        profile.avatar = avatar
        profile.save()
        return redirect("/")  # change to whatever your profile view name is

    return render(request, "users/edit_profile.html", {"profile": profile})
