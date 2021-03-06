"""
Django settings for logbook project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0_vqcr++*a@3n*4d$+!$p_&kcw(j21qiwt)*y^4neo&6=c(0vs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'accounts',
    'flights',
    'pages',
    'dashboard',
    'aircrafts',
    'widget_tweaks',
    'social_auth',
    'user_settings',
    'crews',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'logbook.urls'

WSGI_APPLICATION = 'logbook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Montevideo'

USE_I18N = True

USE_L10N = True

USE_TZ = False


STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
)

AUTH_USER_MODEL = 'accounts.User'

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'social_auth.context_processors.social_auth_login_redirect',

)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/dashboard/'
LOGIN_REDIRECT_URL = '/login/'
LOGIN_ERROR_URL = '/login/'

TWITTER_CONSUMER_KEY = 's3BsHMjPLtCY9goKVeMXyjhsR'
TWITTER_CONSUMER_SECRET = 'c0ljEgvL76BdvdB4uCzMKqL0KvDfTgdMlsggxAskMVSmLNMv5R'

# TODO Register App in Facbook and Linkedin to expand social auth experience
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET = ''

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'twitter', 'linkedin')