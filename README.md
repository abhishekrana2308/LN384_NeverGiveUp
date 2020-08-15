# power-sih-2020
A web App to automatically fetch real time data from various power stakeholders, displays them on the dashboard and provides you with other cool features of automatically triggering and e-mailing.

## command line instructions for linux(ubuntu/mint) only, window users follow the steps and find the commands on your own.
#### install python3
#### install pip3 or install python3-pip
#### install virtualenv
- sudo apt install virtualenv
- pip3 install virtualenv or python3-pip install virtualenv
#### create virtual environment
- virtualenv --no-site-packages django_env --python=python3
#### activate environment
- source django_env/bin/activate
- .\django_env\Scripts\activate (for Windows)
#### install env requirements
- move to folder containing requirements.txt
- pip install -r requirements.txt
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
#### Comments Here
