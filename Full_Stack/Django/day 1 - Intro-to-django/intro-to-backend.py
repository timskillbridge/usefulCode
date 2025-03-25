
'''
Django is a backend framework operating in python

Model View Controller backend web app artchitecture

Django allows for dynamic apis to use in web apps, connecting to databases for data.

Review of HTTP Requests or 'Verbs'
-----------------------------------
GET: Requests data
POST: Create data
PUT: Modify data
DELETE: Delete data

Follows the CRUD format.

Python Virtual Environments
----------------------------
create one:  usually one per project
    python -m venv .venv
creates .venv folder in current directory

Activate it:
    source .venv/bin/activate
De-activate it:
    deactivate

Install Django
---------------------------
upgrade pip:  
    pip install --upgrade pip
install django
    pip install django
Check installed dependencies
    pip freeze
drop requirements.txt file
    code requirements.txt
    pip install -r requirements.txt
create .gitignore
    code .gitignore
        add whatever you want to ignore

                                tart building the App
------------------------------------------------------
run django-admin
    lots of commands
    django-admin help startproject
start a project
    django-admin startproject pokedex_proj
delete project
    rm -rf pokedex_proj
start project within current directory
    django-admin startproject pokedexPorj .
                                        **DON'T MESS WITH manage.py
create your app
    python manage.py startapp pokemon_app
        name your apps <name>_app
add app to settings.py
    django installed_apps
        "pokemon_app"
create database
    createdb pokedex_db (from command line)
    CREATE DATABASE pokedex_db (from within psql)
modify settings.py to use your database
    "Engine": "django.db.backend.postgresql",
    "NAME": "pokedex_db" (or whatever your db is)
install psychopg
    pip install "psycopg[binary]"
update requirements via pip freeze
run server
    python manage.py runserver

'''

'''
Build a django model to build a class
build migration
    python manage.py makemigrations
migrate
    python manage.py migrate

Example class
'''
from django.db import models
class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField(default=1)

'''
django shell
    python manage.py shell
        allows you to write django code in the shell
    from pokemon_app.models import Pokemon,Moves
    pikachu = Pokemon(name= 'Pikachu', level = 12)
        creates pikachu object
    pikachu.save()
        loads picachu's current iteration into database
'''

class Student(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True)

    def __repr__(self):
        return f"{self.id}: {self.first_name}, {self.last_name}"
    
'''
Assign data

create directory called fixtures within the app
    create a json in the directory

    json is an array of objects

    pokemon example: pokemon_data.json

    [
    {
        "model": "pokemon_app.pokemon",
        "pk":1,   <--------pk means primary key
        "fields": {
            "name":"Pikachu",
            "level":12,
            "captured":false
        }
    }
    ]

    python manage.py loaddata pokemon_data.json
'''

class Pokemon(models.Model):
    name=models.CharField(max_length=255)
    level= models.IntegerField(default=1)
    captured = models.BooleanField(default=False)

    def __repr__(self):
        return f"{self.id}: {self.name} {self.level}"
    
    def level_up(self):
        self.level +=1
        self.save()

    def change_captured_status(self):
        self.captured = not self.captured
        self.save()

'''
python manage.py shell
from pokemon_app.models import Pokemon
poke1 = pokemon.objects[0]
poke1
    returns the id, name, and level of the pokemon
'''

'''
django admin

in admin.py

import models
'''
# in admin.py for the app
from django.contrib import admin
from .models import Pokemon

admin.site.register(Pokemon)

'''
test apps by running 
    python manage.py test <app name>

'''
# configure the admin site.  go to the app's admin.py

from django.contrib import admin
from .models import TestModel

#  create superuser
# python manage.py createsuperuser

# modify admin.py to include something like
admin.site.register([Owner,Dog,Bird,Cat,Exotic_Animal])
# where each item in the array is a model

# mod urls.py if needed
# python manage.py runserver

# open /admin and login.