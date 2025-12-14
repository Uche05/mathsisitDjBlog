# Create your views here.
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, PostForm, RegisterForm
from .models import Post


def home(request):
    latest_posts = Post.objects.filter(status="published").order_by("-created_at")[:6]
    return render(request, "main/home.html", {"latest_posts": latest_posts})


def post_list(request):
    posts = Post.objects.filter(status="published").order_by("-created_at")
    return render(request, "main/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status="published")
    return render(request, "main/post_detail.html", {"post": post})


@login_required
def dashboard(request):
    my_posts = Post.objects.filter(author=request.user).order_by("-created_at")
    return render(request, "main/dashboard.html", {"my_posts": my_posts})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully.")
            return redirect("dashboard")
        messages.error(request, "Please fix the errors below.")
    else:
        form = PostForm()

    return render(
        request,
        "main/post_form.html",
        {"form": form, "form_title": "Create a new post"},
    )


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Permission: only owner or staff
    if not (request.user == post.author or request.user.is_staff):
        messages.error(request, "You do not have permission to edit this post.")
        return redirect("dashboard")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect("dashboard")
        messages.error(request, "Please fix the errors below.")
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "main/post_form.html",
        {"form": form, "form_title": "Edit post"},
    )


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if not (request.user == post.author or request.user.is_staff):
        messages.error(request, "You do not have permission to delete this post.")
        return redirect("dashboard")

    # If you want a delete confirmation page, use GET to show it.
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect("dashboard")

    return render(request, "main/post_confirm_delete.html", {"post": post})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created. Please log in.")
            return redirect("login")
        messages.error(request, "Please fix the errors below.")
    else:
        form = RegisterForm()

    return render(request, "main/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("dashboard")
        messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm(request)

    return render(request, "main/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")
