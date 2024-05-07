# Python ML Project 

A Python Machine Lerning project for predicting book ratings or quality using regression and classification Machine Learning methods. 

# Project structure


## .github 

This directory contains the workflows file handling the Continuous Integration (CI) on Github at server side: 

- **ci.yml** 
 

## Data

This directory contains the data file: 

- **books.csv:** The data provided by the project organizer to train the Machine Lerning (ML)models, and it is a curation of **Goodreads** books, based on real user information.
- Dataset attributes: 
    1. bookID: A unique identification number for each book.
    2. title: The name under which the book was published.
    3. authors: The names of the authors of the book.
    4. average_rating: The average rating of the book received in total.
    5. isbn: Another unique number to identify the book, known as the International Standard Book Number.
    6. isbn13: A 13-digit ISBN to identify the book.
    7. language_code: Indicates the primary language of the book. For instance, “eng” is standard for English.
    8. num_pages: The number of pages the book contains.
    9. ratings_count: The total number of ratings the book received.
    10. text_reviews_count: The total number of written text reviews the book received.
    11. publication_date: The date the book was published.
    12. publisher: The name of the book publisher.

The data preprocessing is performed in the file Project1Code.py


## PythonMLProj 

This folder contains the final files required for the transformation of the variables and implementation of the selected model, product of the training performed. In addition, the jupyter notebook containing the process of data cleaning and analysis, as well as model analysis and training is also in this folder, in addition to some other files required for the deployment of the model on the web.

- **books.csv:** The dataset.

- **RF_DataTransform.joblib** The dump of the transformers used during the model training.

- **modelRF.joblib** The dump of the trained model.

- **Project1Code** The code for Exploratory Data Analysis, Models ttraining and evaluation. (Install required libraries from requirements.txt before running this notebook).

- **__init__, asgi, forms, settings, urls, views, wsgi** files used to make the web app work.
 

## Report 

This directory contains the report file, which summarizes the analysis process followed, the methods implemented and the results obtained. 

- **Project_report:** The reports of the project.  


## templates

This directory contains the templates used for the Front end of the web application. 


## Other files

- **.gitignore** The file to be ignored (not tracked) by Git.
- **db.sqlite3** The database of the web application.
- **manage.py** Management script of the web application (e.g. to run the web app server).
- **requirements** Requirements needed in terms of libraries, to make the project working.


# Usage

## Installation

The python notebook Project1Code.py was created using the Python versions 3.11.5. 

To run the project it is possible to create an environment from the requirements.txt file with command:
- python -m venv <virtual_environment_name> <virtual_environment_folder_path>
- Go to the virtual environment folder then go to the folder Scripts/
- Run : activate.bat
- Go to the folder of the file requirements.txt
- Run : pip install -r requirements.txt

The requirements file works on Windows. For Linux, no test was made. 

Once the requirements are ready, to explore this project open the Project1Code.py, and everything is ready so that data can be consumed from there.


## Model Deployment

To run the Wep App, after cloning the project:
- Install required libraries from the requirements.txt file.
- Open a Terminal.
- Run the Web App Server with the command 'python manage.py runserver'.
- From the web navigator,open the URL http://127.0.0.1:xxxx/ displayed in the terminal where you did the previous step.
