"""
Django settings for mycloud project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ei(v1mrl=&*qdxbo3xv=g!+26&zoi*+*ly3q$3@hkso_1%ep88"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    'rest_framework.authtoken',
    "corsheaders",
    "server",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # Должен быть первым для обеспечения безопасности.
    "django.middleware.csrf.CsrfViewMiddleware",  # Защита от CSRF-атак.
    "django.contrib.sessions.middleware.SessionMiddleware",  # Управление сессиями.
    "corsheaders.middleware.CorsMiddleware",  # Должен идти до CommonMiddleware, чтобы CORS заголовки добавлялись к ответам.
    "django.middleware.common.CommonMiddleware",  # Обработка общих запросов, таких как перенаправления.
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Управление аутентификацией.
    "django.contrib.messages.middleware.MessageMiddleware",  # Работа с сообщениями.
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Защита от clickjacking.
]

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",  # Должен быть первым для обеспечения безопасности.
#     "django.contrib.sessions.middleware.SessionMiddleware",  # Управление сессиями.
#     "django.middleware.common.CommonMiddleware",  # Обработка общих запросов, таких как перенаправления.
#     "django.middleware.csrf.CsrfViewMiddleware",  # Защита от CSRF-атак.
#     "django.contrib.auth.middleware.AuthenticationMiddleware",  # Управление аутентификацией.
#     "django.contrib.messages.middleware.MessageMiddleware",  # Работа с сообщениями.
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Защита от clickjacking.
#     "corsheaders.middleware.CorsMiddleware",  # Должен идти до CommonMiddleware, чтобы CORS заголовки добавлялись к ответам.
# ]

ROOT_URLCONF = "mycloud.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mycloud.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'diplom',
        # 'NAME': 'diplom_serv',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    "http://localhost:5173",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
	'DEFAULT_RENDERER_CLASSES': [
		'rest_framework.renderers.JSONRenderer',
	],
}

AUTH_USER_MODEL = 'server.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Стандартный бэкенд
]

STATIC_URL = "/static/"
MEDIA_ROOT = BASE_DIR / 'uploads'
MEDIA_URL = '/uploads/'