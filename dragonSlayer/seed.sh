#!/bin/bash

rm -rf dragonslayerapi/migrations
rm db.sqlite3
python manage.py makemigrations dragonslayerapi
python manage.py migrate
python manage.py loaddata dungeons
python manage.py loaddata professions
python manage.py loaddata playerclasses
python manage.py loaddata bossstatuses
python manage.py loaddata users
python manage.py loaddata tokens


