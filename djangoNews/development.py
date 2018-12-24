from djangoNews.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangonews_ts',
        'USER': 'david',
        'PASSWORD': '123',
        'HOSt': 'localhost',
        'PORT': '5432',
    }
}
