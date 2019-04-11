from . import util
from .models import Movie, MovieReview
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from .forms import MovieReviewForm


def index(request):
    '''Show a list of all movies. Click on a movie to view it'''
    movies = Movie.objects.all()
    return render(request, 'portal/index.html', {'movies':movies})


def show_movie(request, movie_id):
    '''Show the given movie, or raise a 404 error'''
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = movie.moviereview_set.all()
    return render(request, 'portal/show_movie.html', {'movie':movie, 'reviews': reviews})
  

def show_review(request, review_id):
    '''Show the given review, or raise a 404 error'''
    review = get_object_or_404(MovieReview, pk=review_id)
    return render(request, 'portal/show_review.html', {'review':review})
 
def search_reviews(request):
    '''Search for reviews using POST data.
    Use a Form object to handle the form and its input.
    If the form does not validate, redirec to the index page.'''
    if request.method == 'POST':        
        reviews = util.search_reviews_with_text(request.POST['search_text'])
        print(reviews)
        print(reviews[0].movie.title)
        # print(reviews.keys())
        return render(request, 'portal/show_reviews.html', {'reviews':reviews, 'search_text': request.POST['search_text']})
        # print(request[POST].keys())

def manage_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        print(request.POST)
        movie_review_form = MovieReviewForm(request.POST)
        movie_review_form.movie = movie
        movie_review_form.user = request.user
        print('a') 
        print(movie_review_form.movie)
        print(movie_review_form.user)
        # print(movie_review_form.text)
        # print(movie_review_form.title)
        # print(movie_review_form.rating)
        if movie_review_form.is_valid():
            review = movie_review_form.save(commit=False)
            # review.user = request.user
            # review.movie = movie
            review.save()
            reviews = movie.moviereview_set.all()
            return render(request, 'portal/show_movie.html', {'movie':movie, 'reviews': reviews})
        else:
            print(movie_review_form.errors)
            return render(request, 'portal/manage_review.html', 
            {'movie': movie,
            'movie_review_form': movie_review_form})   
    else:
        movie_review_form = MovieReviewForm(
            initial={'movie':movie})
        # movie_review_form.movie = movie
        # print(movie_review_form.movie)
    # print(movie_review_form)
        return render(request, 'portal/manage_review.html', 
        {'movie': movie,
        'movie_review_form': movie_review_form})   
    # Add a new MovieReview object for the given Movie.
    # GET: display the page with an empty form.
    # POST: validate the form. If valid, save the form.
    #       (Add the User to the MovieReview after you call save(False).
    #       Then call save() with no arguments.)
    #       If not valid, render the invalid form.
    #       Be sure to validate the movie as well.'''

def edit_review(request, review_id):
    print('a')
    moviereview = get_object_or_404(MovieReview, pk=review_id)
    print('b')
    movie = get_object_or_404(Movie, pk=moviereview.movie.id)
    if request.method == 'POST':
        print(request.POST)
        movie_review_form = MovieReviewForm(request.POST)
        movie_review_form.movie = movie
        movie_review_form.user = request.user
        print('a') 
        print(movie_review_form.movie)
        print(movie_review_form.user)
        # print(movie_review_form.text)
        # print(movie_review_form.title)
        # print(movie_review_form.rating)
        if movie_review_form.is_valid():
            review = movie_review_form.save(commit=False)
            # review.user = request.user
            # review.movie = movie
            review.save()
            reviews = movie.moviereview_set.all()
            return render(request, 'portal/show_movie.html', {'movie':movie, 'reviews': reviews})
        else:
            print(movie_review_form.errors)
            return render(request, 'portal/manage_review.html', 
            {'movie': movie,
            'movie_review_form': movie_review_form})   
    else:
        print('c')
        movie_review_form = MovieReviewForm(
            initial={'movie':movie,
            'user': request.user,
            'title': moviereview.title,
            'rating': moviereview.rating,
            'text': moviereview.text})
        print(movie_review_form)
        # movie_review_form.movie = movie
        # print(movie_review_form.movie)
    # print(movie_review_form)
        return render(request, 'portal/manage_review.html', 
        {'movie': movie,
        'movie_review_form': movie_review_form})   