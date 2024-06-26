"""
URL configuration for goodmovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movies import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.user_profile, name="user_profile"),
    path("accounts/signup/", views.user_signup, name="user_signup"),

    path("admin/", admin.site.urls),
    path("", views.hello_world, name="index"),
    path("filmy/", views.list_movies, name="list_movies"), 
    path("filmy/<int:pk>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("filmy/nowy/", views.MovieCreateView.as_view(), name="movie_create"),
    path("filmy/<int:pk>/edycja/", views.MovieUpdateView.as_view(), name="movie_update"),
]
