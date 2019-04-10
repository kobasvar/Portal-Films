#!/usr/bin/env python3

import os
import random
import django
from faker import Faker
from random import randint
import imdb


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviews.settings')

django.setup()

from django.contrib.auth.models import User
from portal.models import Movie, MovieReview, MovieReviewComment, MovieReviewVote


def create_users(delete=False):
    if delete:
        User.objects.all().delete()

    users = [
        {
            'first_name': 'Albert',
            'last_name': 'Einstein',
            'password': 'e=mc^2'
        },
        {
            'first_name': 'Marie',
            'last_name': 'Curie',
            'password': 'radioact'
        },
        {
            'first_name': 'Edward',
            'last_name': 'Jenner',
            'password': 'vaccines'
        }
    ]

    for user in users:
        first = user['first_name']
        last = user['last_name']
        username = first[0].lower() \
            + '_' + last.lower()
        email = username + "@science.fake"
        password = user['password']

        user_obj = User.objects.create_user(
            username, email, password)
        user_obj.first_name = first
        user_obj.last_name = last
        user_obj.save()


def create_movies(delete=False):
    if delete:
        Movie.objects.all().delete()

    im = imdb.IMDb()
    movies = im.get_top250_movies()[0:10]
    for movie in movies:
        print('updating %s' % movie['title'])
        im.update(movie, ['main'])
        m = Movie(title=movie['title'], cover_url=movie['cover url'], year=movie['year'])
        m.save()
        # print(movie.keys())
    print('done')
        # To do: use the data in `movie` to populate a
        # new Movie object, then save it.
        # movie = titleid, title, cover url


def create_reviews(delete=False):
    if delete:
        MovieReview.objects.all().delete()

    fake =Faker()
    list = Movie.objects.all()
    for e in list:
        print('pk')
        print(e.pk)
    for i in range(11,20):
        user = User.objects.get(pk=randint(7,9))
        # print(i % 20 + 11)
        movie = Movie.objects.get(pk=i)
        text = fake.text()
        rating = randint(1,10)
        title = fake.text()
        r = MovieReview(user=user,movie=movie,text=text,rating=rating, title=title)
        r.save()
    #         user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    # text = models.TextField(blank=True, null=True)
    # rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    # To do: create at least one review for each movie.


def create_comments(delete=False):
    if delete:
        MovieReviewComment.objects.all().delete()

    # To do: create movie comments


def create_votes(delete=False):
    if delete:
        MovieReviewVote.objects.all().delete()

    # To do: create movie votes (up/down)


# create_users(True)
# create_movies(True)
# MovieReview.objects.all().delete()
# create_reviews(False)
# create_comments(True)
# create_votes(True)
