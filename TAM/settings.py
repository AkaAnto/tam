import os
from datetime import timedelta
from pathlib import Path

import dj_database_url
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env_vars.get('SECRET_KEY')
DEBUG = env_vars.get('DEBUG', False)  == 'True'
ALLOWED_HOSTS = env_vars.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'users',
    'customers',
    'oauth2_provider',
    'rest_framework',
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

ROOT_URLCONF = 'TAM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'TAM.wsgi.application'

# Local, no docker
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Local, using docker
if env_vars.get('USE_DOCKER', False) == 'True':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env_vars.get('POSTGRES_DB', 'postgres'),
            'USER': env_vars.get('POSTGRES_USER', 'postgres'),
            'PASSWORD': env_vars.get('POSTGRES_PASSWORD', 'postgres'),
            'HOST': env_vars.get('POSTGRES_HOST', 'localhost'),
            'PORT': env_vars.get('POSTGRES_PORT', '5432'),
        }
    }
# Prod
if env_vars.get('DATABASE_URL', False):
    DATABASES = {
        'default': dj_database_url.parse(env_vars.get('DATABASE_URL'))
    }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': int(env_vars.get('API_RESPONSE_PAGE_SIZE', 10))
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(env_vars.get('JWT_TOKEN_LIFETIME_MINUTES', 5))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(env_vars.get('JWT_TOKEN_REFRESH_LIFETIME_DAYS', 1))),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": env_vars.get('SECRET_KEY'),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

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
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/api/customers'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATICFILES_LOCATION = "static"
MEDIAFILES_LOCATION = "media"
AWS_STORAGE_BUCKET_NAME = env_vars.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = env_vars.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env_vars.get('AWS_SECRET_ACCESS_KEY')
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"
STORAGES = {
    "default": {"BACKEND": "TAM.custom_storage.MediaStorage"},
    "staticfiles": {"BACKEND": "TAM.custom_storage.StaticStorage"},
}
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=2592000",
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
