#!/bin/bash

rm -rf kennywoodapi/migrations
rm db.sqlite3
python manage.py makemigrations kennywoodapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata visitors
python manage.py loaddata targetpopulation
python manage.py loaddata parkarea
python manage.py loaddata attractioncategory
python manage.py loaddata attraction
python manage.py loaddata attractionrating
python manage.py loaddata itinerary