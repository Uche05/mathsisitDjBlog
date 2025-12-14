from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post_list, name="post_list"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("posts/new/", views.post_create, name="post_create"),
    path("posts/<slug:slug>/edit/", views.post_edit, name="post_edit"),
    path("posts/<slug:slug>/delete/", views.post_delete, name="post_delete"),
    path("posts/<slug:slug>/", views.post_detail, name="post_detail"),
    
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]