TDS Assignment 5 - I

Installation

Open settings.py file in the Django project and navigate to the databases section . Replace the  values with appropriate details. example below.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'your_database_name',
        "USER": 'your_username',
        "PASSWORD": 'your_password',
        "HOST": 'localhost',
        "PORT" : '5432'
    }
}

Navigate to the install apps section and make sure to add rest_framework and coursesApi.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'coursesApi',
    'rest_framework'
]

Install required external library:
pip install beautifulsoup4
pip install psycopg2

Run the server:
python manage.py runserver




