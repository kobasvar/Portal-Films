from django import forms
from django.forms import TextInput, Textarea
from .models import MovieReview


class SearchForm(forms.Form):
    search_text = forms.CharField(
        label='Search',
        max_length=100,
        widget=TextInput(attrs={
            'class': "form-control mr-sm-2",
            'type': "search"
        })
    )

class MovieReviewForm(forms.ModelForm):
	class Meta:
		model = MovieReview
		fields = ['movie','title','text','rating']
		widgets = {'movie': forms.HiddenInput()}


# class AddReviewForm(forms.Form):
# 	title = forms.CharField()
# 	text = forms.CharField(widget=Textarea)
#     # title = forms.CharField(
#     #     label='Title',
#     #     max_length=50,
#     #     widget=TextInput(attrs={
#     #         'class': "form-control mr-sm-2",
#     #         'type': 'text'
#     #     })
#     # )
#     # text = forms.CharField(
#     # 	label='Text',
#     # 	max_length=100,
#     # 	widget=Textarea(attrs={
#     #         'class': "form-control mr-sm-2",
#     #         'type': 'text'
#     #     })
#     # )
