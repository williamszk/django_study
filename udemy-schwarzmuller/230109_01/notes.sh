

pip3 install Django
pip install tzdata

django-admin startproject django_course_site
cd django_course_site

python3 manage.py startapp meetups 

# about syncronizing the database with models
python3 manage.py makemigrations
python3 manage.py migrate 

# Create an admin user
python3 manage.py createsuperuser
admin
123







