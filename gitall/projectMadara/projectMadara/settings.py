"""
Django settings for projectMadara project.
Generated by 'django-admin startproject' using Django 1.10.
For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
# import key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dbnlnq%h(c*mgpzata%*wf9pys$2!(5#h6=g!$x56=zd^0xg&-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'gitall.tech']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'analytics',
    'comments',
    'contact',
    'main',
    'slack_invite',
    'shell',
    'wiki',
    'write',
    'tags',

    # 3rd party softwares
    'crispy_forms',
    'mediumeditor',
    'phonenumber_field',

    # for aws storage
    'storages',
    # django all auth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projectMadara.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'projectMadara.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
       'default': {
             'ENGINE':'django.db.backends.postgresql_psycopg2',
             'NAME': os.environ['RDS_DB_NAME'],
             'USER': os.environ['RDS_USERNAME'],
             'PASSWORD': os.environ['RDS_PASSWORD'],
             'HOST': os.environ['RDS_HOSTNAME'],
             'PORT': os.environ['RDS_PORT'],
             }
          }
else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gitalldb',
            'USER': 'gitalluser',
            'PASSWORD': 'gitall@12345',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'database'),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# This would work only where the DEBUG mode us true
# if DEBUG:
MEDIA_URL = '/media/'

#
# everything after collectstatic goes here
# where django looks for static files after production
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_pro")

#
# this is where django looks for the static files during development
# this is where the user must keep his static files
STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
]
#
# user generated media is stored here
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")


SITE_ID = 2


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


#
# e-mail settings
EMAIL_HOST = "email-smtp.us-west-2.amazonaws.com"
EMAIL_HOST_USER = "AKIAI3ZVUWYZRLEYRD2Q"
EMAIL_HOST_PASSWORD = "AlzYqjDFAxLJI0P88GNFgOj5zmQ1XYzMgg3NMD72Km8v"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Crispy Template Pack
CRISPY_TEMPLATE_PACK = "bootstrap3"

# django all-auth settings
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/"

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "My Subject"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_SIGNUP_FORM_CLASS = None
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_BLACKLIST = ["hasime", "iamhasime", "update", "admin", "update"]
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


# This will tell boto that when it uploads files to S3,
# it should set properties on them so that when S3 serves them,
# it'll include some HTTP headers in the response.
# Those HTTP headers, in turn, will tell browsers that they can cache these files for a very long time.

"""
    During development, keep the below code commented.
"""
# AWS_S3_OBJECT_PARAMETERS = {
#     'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#     'CacheControl': 'max-age=94608000',
# }

# AWS_STORAGE_BUCKET_NAME = 'gitall'
# AWS_S3_REGION_NAME = 'us-west-2'  # e.g. us-east-2
# AWS_ACCESS_KEY_ID = 'AKIAJNGHFR4TFMKOTWCQ'
# AWS_SECRET_ACCESS_KEY = 'S/l5wsZxJ4FeLWWZQuTPjzouOPOapcsvgCfIA9Fc'

# # Tell django-storages the domain to use to refer to static files.
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# # Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# # you run `collectstatic`).
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# # From ../custom_storages.py
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'

# MEDIAFILES_LOCATION = 'media'
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'


"""
    Phone no default field
        - from phonenumberfield
"""
PHONENUMBER_DEFAULT_REGION = '+91'


"""
    Medium Editor Text Editor settings
"""
MEDIUM_EDITOR_THEME = 'bootstrap'
MEDIUM_EDITOR_OPTIONS = {
    'toolbar': {
        'static': False,
        'buttons': [
            'bold',
            'italic',
            'pre',
            'underline',
            'quote',
            'orderedlist',
            'strikethrough',
            'h2',
            'h3',
            'image',
        ]
    },
    'paste': {
        'forcePlainText': True,
        'cleanPastedHTML': False,
        'cleanReplacements': [],
        'cleanAttrs': ['class', 'style', 'dir'],
        'cleanTags': ['meta']
    }
}
