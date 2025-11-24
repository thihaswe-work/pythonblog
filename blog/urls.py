from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/create/", views.create_post, name="create_post"),
    path("post/<slug:slug>/delete/", views.delete_post, name="delete_post"),
    path("post/<slug:slug>/edit/", views.edit_post, name="edit_post"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.create_category, name="create_category"),
    path("categories/edit/<int:category_id>/", views.edit_category, name="edit_category"),
    path("categories/delete/<int:category_id>/", views.delete_category, name="delete_category"),

]
