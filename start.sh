#!/bin/bash
flask db migrate
flask db upgrade
gunicorn -w 4 -b 0.0.0.0:10000 wsgi:app
