"""A basic database set-up for Travis CI.

The set-up uses the 'TRAVIS' (== True) environment variable on Travis
to detect the session, and changes the default database accordingly.

Be mindful of where you place this code, as you may accidentally
assign the default database to another configuration later in your code.
"""

import os

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travis_ci_test',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'develop',
            'USER':     'develop',
            'PASSWORD': 'develop',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }


SECRET_KEY = 'qwerty?'

INSTALLED_APPS = (
    'amqp_2phase',
    'tests',
)

import django
django.setup()