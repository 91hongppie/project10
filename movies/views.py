from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST  # post 요청만 받아준다..
from .models import Movie, Review
from .forms import MovieForm, ReviewForm

def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies,}
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {'form': form,}
    return render(request, 'movies/form.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    review_form = ReviewForm()
    context = {'movie': movie, 'reviews':reviews, 'review_form':review_form,}
    return render(request, 'movies/detail.html', context)
