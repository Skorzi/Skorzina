#!/bin/bash
source /root/danilenter/Skorzina/activate
exec gunicorn -c '/root/danilenter/Skorzina/gunicorn_config.py' Skorzina.wsgi
