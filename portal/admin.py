from django.contrib import admin
from .models import Movie, MovieReview

# to do: register models for Admin app to use

# Register your models here.

admin.site.register(Movie)
admin.site.register(MovieReview)
