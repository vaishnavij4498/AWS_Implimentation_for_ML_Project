from flask import Flask,render_template,request
#import pickle
import numpy as np
import pandas as pd
from datetime import datetime
from joblib import load

#dfmodel = pickle.load(open('c:/Users/vaish/Projects/PythonMLProj/ML_Model_deployment/model.pkl','rb'))
#dftransform = pickle.load(open('c:/Users/vaish/Projects/PythonMLProj/ML_Model_deployment/RF_DataTransform.pkl','rb'))
dfmodel = load(open('c:/Users/vaish/Projects/PythonMLProj/ML_Model_deployment/modelRF.joblib','rb'))
dftransform = load(open('c:/Users/vaish/Projects/PythonMLProj/ML_Model_deployment/RF_DataTransform.joblib','rb'))
#RF = joblib.load('regression_model.joblib')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_book_rating():
    #title = str(request.form.get('title'))
    #authors = str(request.form.get('authors'))
    num_pages = int(request.form.get('num_pages'))
    text_reviews_count = int(request.form.get('text_reviews_count'))
    publicationYear = int(request.form.get('publicationYear'))
    language_code_grouped = str(request.form.get('language_code_grouped'))
    #language_mapping = {'eng': 1, 'spa': 2, 'fre':3, 'spa':4, 'ger':5, 'jpn':6, 'other':7}  # Add other language codes as needed
    #numeric_language = ['eng','spa', 'fre', 'spa', 'ger', 'jpn', 'other'] 
    #numeric_language = 'eng' # Example value
    #language_code_grouped = language_mapping.get(numeric_language, 0)  # Default to 0 if not found
    author_number_books = int(request.form.get('author_number_books'))

    #Tranformdata
    #prediction
    bookdata = [[num_pages, text_reviews_count, publicationYear, language_code_grouped, author_number_books]]
    dfbookdata = pd.DataFrame(bookdata, columns=['num_pages', 'text_reviews_count', 'publicationYear', 'language_code_grouped', 'author_number_books'])
    #dfbookdata = np.array([num_pages,text_reviews_count,publicationYear,language_code_grouped,author_number_books])
   
    bookdata_transform = dftransform.transform(dfbookdata)
    
    result = dfmodel.predict(bookdata_transform)
    #result = dfmodel.predict(np.array([num_pages,text_reviews_count,publicationYear,language_code_grouped,author_number_books]).reshape(1,9))
    
    if result == 1:
        result = 'HighlyRated'
        
    else:
        result = 'LowRated!'
        

    return render_template('index.html',result=result)
    
if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0',port=8080)