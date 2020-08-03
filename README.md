# LN384_NeverGiveUp
## command line instructions for linux(ubuntu/mint) only, window users follow the steps and find the commands on your own

#### Install python3

#### Install pip

#### Install django
- pip install django==1.9

#### running django server
- move to folder containing manage.py file
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

#### Creating Super User
- move to folder containing manage.py file
- python manage.py createsuperuser
- Enter username and password

#### Django Admin
- First create a super user
- move to folder containing manage.py file
- python manage.py runserver
- Go to localhost:8000/admin

