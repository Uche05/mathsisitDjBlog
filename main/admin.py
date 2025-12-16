from django.contrib import admin
from .models import Profile, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # keep your useful admin features
    list_display = ("title", "author", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("title", "content", "author__username")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",) 
    # enable summernote for content field

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "approved", "created_at")
    list_filter = ("approved", "created_at")
    search_fields = ("content", "author__username", "post__title")
