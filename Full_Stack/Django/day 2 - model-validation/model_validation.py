
'''
MODEL VALIDATION
---------------------------------

Review:

1. Virtual env
deactivate
python -m venv .venv
source .venv/bin/activate

2. Install Django and psycopg
pip install --upgrade pip
pip install django
pip install "psycopg[binary]"

3. start building the App
django-admin startproject <proj name> .
python manage.py startapp <app_name_app>

4. modify settings.py
    "pokemon_app"
    "Engine": "django.db.backend.postgresql",
    "NAME": "pokedex_db" (or whatever your db is)

5. create db
createdb <database_name_db>



6. create requirements file
pip freeze
    code requirements.txt
        freeze contents

7. run server
python manage.py runserver

8. buidl model classes and fixtures if appliccable
    mkdir fixtures
        build json
        [{
        "model": "<model to be applied>",
        "pk":1,
        "fields": {
            "name":"Pikachu",
            "level":12,
            "captured":false
        }
        }]
    python manage.py loaddata <fixutre json>
    python manage.py makemigrations
    python manage.py migrate
'''

'''
FIELD VALIDATION WITH VALIDATORS
--------------------------------
Validators will act like postgresql checks and will be run PRIOR TO SQL ACTION
    - highly structured



1. imports
    from django.core import validators as v (or whatever you want to type a lot)

2. within class elements, call validates using this syntax:
    validators = [v.<validator_name>, v.<validator_name>]
    
3. run self.full_clean() on all methods prior to save

CUSTOM VALIDATOR

create validator.py
import validaiton error class and regex

'''
from django.core.exceptions import ValidaitonError
import re

def validate_name(name):
    error = "impropper name format"
    regex = r'^[A-Z][a-z]*$'
    valid_name = re.match(regex,name)

    if valid_name:
        return name
    else:
        raise ValidaitonError(error_msg,params={'name': name})
    
'''
in models
'''
from .validator import validate_name

'''
add validator to model element

name = models.CharField(max_length=100, validators=[validate_name])

'''

'''TESTS
in new tests.py
'''

from django.test import TestCase
from django.core.exceptions import ValidationError

class pokemon_test(TestCase):

    def test_01_create_pokemon(self):
        new_pokemon = Pokemon(name='Pikachu', description = "Only the best electric type pokemon in existence")

        try:
            new_pokemon.full_clean()
            self.assertIsNotNone(new_pokemon)
        except ValidationError as e:
            self.fail

    def test_01_valid_poke_name(self):
        bad_poke_name = Pokemon(name='pikachu')

        try:
            bad_poke_name.full_clean()
            self.fail
        except ValidaitonError as e:
            print(e.message_dict)
            self.assertTrue('Improper name format' in e.message)

'''
Serializers
    - used in building APIs
    - turn json into objects
    - turns objects into json

    serialize("json",[object])  <--object within list []

django rest framework
install
-------
pip install djangorestframework

modify settings.py to add installed apps "rest_framework"

Building a Serializer
---------------------

create serializers file 'serializers.py
'''
from rest_framework import serializers
#from .models import <model>

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = '<model>'   #<--your model name
        fields = [
            'id',
            'name',
            'level'
        ]

'''
run python shell
    python manage.py shell
grab your model
    from pokemon_app.models import Pokemon
grab an object
    pikachu = Pokemon.objects.get(name="Pikachu")
grab serializer
    from pokemon.app.serializers import Pokemon_Serializer
grab object serializer
    pikachu_serialized = PokemonSerializer(Pokemon.objects.get(name='Pikachu'))
data lives in <object>_serialized.data
    pikachu_serialized.data.get('name')
        'Pikachu'

GRAB MULTIPLE OBJECTS
---------------------
all_pokemon = Pokemon.objects.all()
serializer = PokemonSerializer(all_pokemon, many=True)

CREATE Object from dictionary  <--within the python manage.py shell
ditto = {"name" : "Ditto", "level":3}
--------------------
serialized_ditto = PokemonSerializer(data = ditto)
serialized_ditto.is_Valid()
serialized_ditto.save()

'''

