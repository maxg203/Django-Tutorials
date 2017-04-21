from tutorial.settings.base import *

# Override base.py settings here
DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


try:
    from tutorial.settings.local import *
except:
    pass
