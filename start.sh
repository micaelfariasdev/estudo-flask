#!/bin/bash
flask db migrate
gunicorn app:application --bind 0.0.0.0:$PORT
