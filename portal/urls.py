from django.urls import path

from . import views

app_name = 'portal'

urlpatterns = [
	path('', views.index, name='index'),
	path('portal/search_results', views.search_reviews, name='search_reviews'),
	path('portal/show_review/<int:review_id>', views.show_review, name='show_review'),
	path('portal/show_movie/<int:movie_id>', views.show_movie, name='show_movie'),
	# path('portal/person/<int:person_id>', views.show_person, name='show_person'),
 #    path('portal/person/add', views.add_person, name='add_person'),
	# path('portal/person/adddata', views.add_person_data, name='add_person_data'),
	# path('portal/person/safe', views.show_safe_persons, name='show_safe_persons'),
	# path('portal/person/search_results', views.search_results, name='search_results'),
    # to do: add more paths...
]