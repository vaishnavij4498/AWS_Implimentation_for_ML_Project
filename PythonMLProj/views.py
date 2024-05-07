from django.http import HttpResponse
from django.shortcuts import render

from PythonMLProj.forms import PredictForm

import pandas as pd
from joblib import load

def predict_ratings_view(request):
    form = PredictForm()

    if request.method == 'POST':
        #Get input variables from the Front End
        form = PredictForm(request.POST)
        if form.is_valid():
            num_pages = form.cleaned_data['num_pages']
            text_reviews_count = form.cleaned_data['text_reviews_count']
            publicationYear = form.cleaned_data['publicationYear']
            language_code_grouped = form.cleaned_data['language_code_grouped']
            author_number_books = form.cleaned_data['author_number_books']

            # Load model and transformer generated during the Model Training
            transformer = load('PythonMLProj\\RF_DataTransform.joblib')
            classifier = load('PythonMLProj\\modelRF.joblib')

            #Format input data so that they can be used by the Machine Learning model
            book_info = [[num_pages, text_reviews_count, publicationYear, language_code_grouped, author_number_books]]
            book_info_df = pd.DataFrame(book_info, columns=['num_pages', 'text_reviews_count', 'publicationYear', 'language_code_grouped', 'author_number_books'])

            #Transform input data and predict
            book_info_df_trans = transformer.transform(book_info_df)
            #book_predict_proba = classifier.predict_proba(book_info_df_trans)
            book_rating_pred = classifier.predict(book_info_df_trans)
            if (book_rating_pred == 1):
                rep = "High rate"
            else:
                rep = "Low rate"
            # Return results to the view to be displayed
            return render(request, 'result-ratings.html', {'num_pages': num_pages, 'text_reviews_count': text_reviews_count, 'publicationYear': publicationYear, 'language_code_grouped': language_code_grouped, 'author_number_books': author_number_books, 'predicted_book_rating': rep})
    return render(request, 'predict_ratings.html', {'form': form})

def home_view(request):
    #return HttpResponse('Hello Word!')
    return render(request, 'home.html')
