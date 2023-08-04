"""
Django settings for Wining project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from django.conf.global_settings import STATICFILES_DIRS
from django.test.signals import static_finders_changed
import mimetypes


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_SAVE_EVERY_REQUEST = True

import os

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# logging
LOGGING = {
    "version": 1.0,
    "disable_existing_loggers": False,
    "formatters": {
        "format1": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s : %(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "format2": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "log/logfile.log"),
            "encoding": "utf-8",
            "maxBytes": 1024 * 1024 * 256,
            "backupCount": 5,
            "formatter": "format1",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "format2",
        },
    },
    "loggers": {
        "django": {"handlers": ["file"], "propagate": True, "level": "WARNING"},
        "django.request": {"handlers": ["file"], "propagate": True, "level": "WARNING"},
        "search": {"handlers": ["file", "console"], "propagate": True, "level": "INFO"},
        "detail": {"handlers": ["file", "console"], "propagate": True, "level": "INFO"},
        "user": {"handlers": ["file", "console"], "propagate": True, "level": "INFO"},
        "board": {"handlers": ["file", "console"], "propagate": True, "level": "INFO"},
        "store": {"handlers": ["file", "console"], "propagate": True, "level": "INFO"},
        "purchasing": {
            "handlers": ["file", "console"],
            "propagate": True,
            "level": "INFO",
        },
        "errorhandling": {
            "handlers": ["file", "console"],
            "propagate": True,
            "level": "INFO",
        },
    },
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t+x=)475)9=g3d_s84v!pps^irv8f$)6wfz@094&^ujxh10beg"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1" ]


# Application definition

INSTALLED_APPS = [
    "mathfilters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "user.apps.UserConfig",
    "board.apps.BoardConfig",
    "bootstrap4",
    "search",
    "detail",
    "store",
    "purchasing",
    "errorhandling",
    "django_extensions",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Wining.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "Wining.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "bit",
        "USER": "bit",
        "PASSWORD": "bit",
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8",
            "use_unicode": True,
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

KAKAO_REST_API_KEY = "3928e19c741cff6d9be9122659cfc5ce"
KAKAO_REDIRECT_URI1 = "http://localhost:8000/user/inputUser"
KAKAO_REDIRECT_URI2 = "http://localhost:8000/user/inputUserInfo"
KAKAO_REDIRECT_URI3 = "http://localhost:8000/user/inputStore"

LOGOUT_REDIRECT_URI1 = "http://localhost:8000/user/locallogout"


mimetypes.add_type("application/javascript", ".js", True)

