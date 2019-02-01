django personal-scheduler
Studies and workouts scheduling app built using Django 

Usage <br>
Clone this repo, setup virtualenv, install Django

git clone https://github.com/huiwenhw/django-calendar
cd django-calendar

virtualenv env
source env/bin/activate
pip3 install -r requirements.txt

python3 manage.py migrate
python3 manage.py runserver
python3 manage.py createsuperuser

run app at http://localhost:8000/
