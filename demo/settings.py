"""
Django settings for demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b!@yz9a1)g%p0hvm3buwanh9q@h&zua1x924=+*6rg8_ds35k-'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = 'DB_NAME' not in os.environ
DEBUG = True
# Define your admin email address here
# ADMINS = (('<Your Name>', '<Your email address>'),)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # heroku deploy dependencies
    'whitenoise.runserver_nostatic'
]

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        # 'TEMPLATE_DEBUG': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


################## Doorsale #########################
# Doorsale e-commerce settings for Django project
# Customize these settings only if you know
from doorsale.settings import *
INSTALLED_APPS += DOORSALE_APPS

# Your email server settings should be define here
# EMAIL_HOST = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''

#Cookie name. this can be whatever you want
SESSION_COOKIE_NAME='tokenname_sessionid'  # use the sessionid in your views code
#the module to store sessions data
SESSION_ENGINE='django.contrib.sessions.backends.db'
#age of cookie in seconds (default: 2 weeks)
SESSION_COOKIE_AGE= 24*60*60*7 # the number of seconds for only 7 for example
#whether a user's session cookie expires when the web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE=False
#whether the session cookie should be secure (https:// only)
SESSION_COOKIE_SECURE=False



# Django JET
JET_DEFAULT_THEME = 'default'
JET_THEMES = [
    {
    'theme': 'default',
    'color': '#47bac1',
    'title': 'Default'
    },
    {
    'theme': 'green',
    'color': '#44b78b',
    'title': 'Green'
    },
    {
    'theme': 'light-green',
    'color': '#2faa60',
    'title': 'Light Green'
    },
    {
    'theme': 'light-violet',
    'color': '#a464c4',
    'title': 'Light Violet'
    },
    {
    'theme': 'light-blue',
    'color': '#5EADDE',
    'title': 'Light Blue'
    },
    {
    'theme': 'light-gray',
    'color': '#222',
    'title': 'Light Gray'
    }
]
# JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
# JET_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'
JET_MODULE_YANDEX_METRIKA_CLIENT_ID = '46de85bff0f94c82bbf42be177f128a2'
JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET = '01107ac1049b49ab9b24e60e95ba2a93'
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(PROJECT_DIR, 'client_secrets.json')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
