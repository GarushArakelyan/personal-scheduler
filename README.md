personal-scheduler<br>
Studies and workouts scheduling app built using Django <br>

Usage <br>
Clone this repo, setup virtualenv, install Django

git clone https://github.com/GarushArakelyan/personal-scheduler <br>

cd personal-scheduler
virtualenv env <br>
source env/bin/activate <br>
pip3 install -r requirements.txt <br>

python3 manage.py migrate <br>
python3 manage.py runserver <br>
python3 manage.py createsuperuser <br>

run app at http://localhost:8000/
