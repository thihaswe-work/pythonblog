from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "created_at")
    list_filter = ("category", "author")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
