apt install python3 python3-venv

python3 -m venv .venv
pip install django
pip install tzdata 

# Source code
# https://github.com/divanov11/Django-2021

django-admin

django-admin startproject devsearch

cd devsearch
# Start server
python3 manage.py runserver

# Create a new App
python3 manage.py startapp projects


python3 manage.py makemigrations
python3 manage.py migrate 


# Create a new admin user
python3 manage.py createsuperuser 
admin
123
y






