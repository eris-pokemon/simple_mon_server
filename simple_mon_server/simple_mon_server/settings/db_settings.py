from simple_mon_server.settings.base_settings import *
"""
See https://docs.djangoproject.com/en/1.9/ref/settings/#databases
Not all of the following are always needed. Comment out the ones that you don't need to use.
For example, postgres can operate on user based auth which on a local dev machine only needs NAME and USER.
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': get_env_var('DB_NAME'),
        'USER': get_env_var('DB_USER'),
        'PASSWORD': get_env_var('DB_PW'),
        'HOST': get_env_var('DB_HOST'),
        'PORT': get_env_var('DB_PORT'),
    }
}
