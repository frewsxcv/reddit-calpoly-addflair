from django.core.handlers.wsgi import WSGIHandler
import uwsgi
import sys 
import os


sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
djangoapp = WSGIHandler()
uwsgi.applications = {'/reddit/calpoly': djangoapp}
