from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from movies.models import Movie


def hello_world(request):
    our_context = {"time": datetime.now()}
    return render(
        request,
        template_name="index.html",
        context=our_context
    )


class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ["title", "short_description", "published_at", "rating"]
    success_url = reverse_lazy("list_movies")


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ["title", "short_description", "published_at", "rating"]
    success_url = reverse_lazy("list_movies")


def list_movies(request):
    movies = Movie.objects.all()
    return render(
        request,
        template_name="movie_list.html",
        context={"movies": movies}
    )


def user_profile(request):
    return render(
        request,
        template_name="registration/profile.html",
        context={"user": request.user}
    )


def user_signup(request):
    if request.method == "POST":
        # tutaj przetwarzamy dane z formularza
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                template_name="registration/signup_complete.html",
            )
        else:
            return render(
                request,
                template_name="registration/signup_form.html",
                context={"form": form}
            )
    else:  # np metoda GET
        # wysyłamy pusty formularz użytkownikowi
        form = UserCreationForm()
    return render(
        request,
        template_name="registration/signup_form.html",
        context={"form": form}
    )