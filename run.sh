#! /bin/sh

cd blank
python3 /blank/manage.py migrate && python3 /blank/manage.py runserver 0.0.0.0:80
