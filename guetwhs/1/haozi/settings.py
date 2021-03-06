# -*- coding: utf-8 -*-
"""
Django settings for wade project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import environ
import django.conf

django.conf.global_settings.SESSION_EXPIRE_AT_BROWSER_CLOSE=True
django.conf.global_settings.SESSION_SAVE_EVERY_REQUEST=True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
debug = not environ.get("APP_NAME","")

if debug:
    MYSQL_DB = 'wade'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'whscfan'
    MYSQL_HOST_M = '127.0.0.1'
    MYSQL_HOST_S = '127.0.0.1'
    MYSQL_PORT = '3306'
else:
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hy)vbn3#^9t$yu(te^mo7090ik@ptxv%q&nt#0@wuv++lvho^u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.sinaapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'haozi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'haozi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER':MYSQL_USER,
        'PASSWORD':MYSQL_PASS,
        'HOST':MYSQL_HOST_M,
        'PORT':MYSQL_PORT,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
# other static file location
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATICFILES_FINDERS=(
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

MEDIA_ROOT = '/media/'

MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'blog.Account'

PER_PAGE_COUNT=5

#log配置###########################################
# LOG_FILE = "./all.log"
#
# LOGGING = {
#         'version': 1,
#         'disable_existing_loggers': True,
#
#         'filters': {
#             'require_debug_false': {
#                 '()': 'django.utils.log.RequireDebugFalse'
#                 }
#             },
#         'formatters': {
#             'simple': {
#                 'format': '[%(levelname)s] %(module)s : %(message)s'
#                 },
#             'verbose': {
#                 'format': '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
#                 }
#             },
#
#         'handlers': {
#             'null': {
#                 'level': 'DEBUG',
#                 'class': 'django.utils.log.NullHandler',
#                 },
#             'console': {
#                 'level': 'INFO',
#                 'class': 'logging.StreamHandler',
#                 'formatter': 'verbose'
#                 },
#             'file': {
#                 'level': 'INFO',
#                 'class': 'logging.handlers.TimedRotatingFileHandler',
#                 'formatter': 'verbose',
#                 'filename': LOG_FILE,
#                 'when':'W0',
#                 'backupCount':500,
#                 },
#             'mail_admins': {
#                 'level': 'ERROR',
#                 'class': 'django.utils.log.AdminEmailHandler',
#                 'filters': ['require_debug_false']
#                 }
#             },
#         'loggers': {
#             '': {
#                 'handlers': ['file', 'console'],
#                 'level': 'INFO',
#                 'propagate': True,
#                 },
#             'django': {
#                 'handlers': ['file', 'console'],
#                 'level': 'DEBUG',
#                 'propagate': True,
#                 },
#             'django.request': {
#                 'handlers': ['mail_admins', 'console'],
#                 'level': 'ERROR',
#                 'propagate': True,
#                 },
#             }
#         }