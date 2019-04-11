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
    movie = Movie.objects.get(pk=movie_id)
    reviews = movie.moviereview_set.all()
    return render(request, 'portal/show_movie.html', {'movie':movie, 'reviews': reviews})
  

def show_review(request, review_id):
    '''Show the given review, or raise a 404 error'''
    review = MovieReview.objects.get(pk=review_id)
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
    # print(movie_id)
    movie_review_form = MovieReviewForm()
    # print(movie_review_form)
    return render(request, 'portal/manage_review.html', 
        {'movie_id': movie_id,
        'movie_review_form': movie_review_form})   

def save_review(request):
    pass
    # print(movie_id)
    # movie_review_form = MovieReviewForm()
    # return render(request, 'portal/manage_review.html', 
    #     {movie_id: movie_id,
    #     movie_review_form: MovieReviewForm})   
# uncomment this line - find the correct import for it!
# @login_required
# def review(request, movie_id):
#     print('add')
#     return render(request, 'portal/_add_review.html', {'movie_id': movie_id})   
#     pass
    '''Add a new MovieReview object for the given Movie.
    GET: display the page with an empty form.
    POST: validate the form. If valid, save the form.
          (Add the User to the MovieReview after you call save(False).
          Then call save() with no arguments.)
          If not valid, render the invalid form.
          Be sure to validate the movie as well.'''
