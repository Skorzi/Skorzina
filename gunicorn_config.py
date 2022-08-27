command = '/usr/local/lib/python3.8/dist-packages/gunicorn'
pythonpath = '/root/danilenter/Skorzina'
bind = '127.0.0.1:8000'
workers = 2
user = 'root'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=Skorzina.settings'
