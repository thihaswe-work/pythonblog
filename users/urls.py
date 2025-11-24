from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),   # add this
    path("<str:username>/posts/", views.user_posts, name="user_posts"),
    path("logout/", views.logout_view, name="logout"),
    path("edit/", views.edit_profile, name="edit_profile"),  # <-- edit profile route

]

