# Recipeweb
recipe book
for this project I installed Django in my pycharm terminal firstly by pip install django
for create project: python manage.py startproject Recipes
create application named recipebook, users, home I run
python manage.py startapp recipebookapp
python manage.py startapp home
python manage.py startapp users
set up settings.py page
create templates for each application folder and its css and image files
create views and corresponding urls for each pages
users templates includes login, logout, registration, create profile, editprofile, view profile  
home templates includes home, nav, card, form pages for viewing firstpage.
recipebookapp template includes create and view pages for create and view recipes.
for migrates data to django admin database run commands: 
python manage.py makemigrations
python manage.py migrates
python manage.py createsuperuser
for running the webapplication run command: python manage.py runserver
