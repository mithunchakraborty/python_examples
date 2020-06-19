from django.shortcuts import render
from django.views.generic.base import View
from .models import *


class MoviesView(View):
    @staticmethod
    def get(request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movie_list': movies})
