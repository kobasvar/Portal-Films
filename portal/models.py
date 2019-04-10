from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    # titleid, title, cover url
    # titleid = models.IntegerField(default=None)
    title = models.CharField(max_length=50, default=None)
    cover_url = models.CharField(max_length=100, default=None)
    year = models.CharField(max_length=4, default=None)
   
    def __str__(self):
        return (self.title)


class MovieReview(models.Model):

    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)

    def __str__(self):
        return (self.text)

    # To do: add the relevant fields.


class MovieReviewVote(models.Model):

    VOTE_CHOICES = (
        ('u', 'Up'),
        ('d', 'Down')
    )

    movie_review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
    value = models.CharField(max_length=1, choices=VOTE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MovieReviewComment(models.Model):
    movie_review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
