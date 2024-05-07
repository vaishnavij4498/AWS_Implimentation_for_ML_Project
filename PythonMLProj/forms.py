from django import forms

class PredictForm(forms.Form):
    num_pages = forms.IntegerField(label='num_pages')
    text_reviews_count = forms.IntegerField(label='text_reviews_count')
    publicationYear = forms.IntegerField(label='publicationYear')
    language_code_grouped = forms.CharField(label='language_code_grouped')
    author_number_books = forms.IntegerField(label='author_number_books')