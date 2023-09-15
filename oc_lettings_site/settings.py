import os

from configparser import ConfigParser
from pathlib import Path

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import environ


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

env = environ.Env(DEBUG=(bool, False))

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env("DEBUG")

SECRET_KEY = env("DJANGO_SECRET_KEY")
sentry_dsn = env("SENTRY_DSN")


"""env_ok = False
try:
    file = os.path.isfile(".env")
    if file:
        print("\t ENV FILE FOUND")
        env_ok = True

except Exception:
    pass

if env_ok:
    env_file = os.path.join(BASE_DIR, ".env")
    config = ConfigParser()
    config.read(env_file)
    django_key = config.get("DJANGO", "DJANGO_SECRET_KEY", raw=True)
    sentry_dsn = config.get("SENTRY", "SENTRY_DSN", raw=True)
else:
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )
    print("\n\tNO ENV file")
    # django_key = os.environ.get("DJANGO_SECRET_KEY")
    django_key = env("DJANGO_SECRET_KEY")
    sentry_dsn = os.environ.get("SENTRY_DSN")"""


"""
if not os.path.isfile("config.ini"):
    with open("config.ini", "w") as env_file:
        config = ConfigParser()
        config["DJANGO"] = {"DJANGO_SECRET_KEY": "django_secret_key"}
        config["SENTRY"] = {"SENTRY_DSN": "sentry_dsn"}
        config.write(env_file)

django_key = os.environ.get("DJANGO_SECRET_KEY")
sentry_dsn = os.environ.get("SENTRY_DSN")
"""

# SECRET_KEY = django_key

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ["*"]


sentry_sdk.init(
    dsn=sentry_dsn,
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)


# Application definition

INSTALLED_APPS = [
    "oc_lettings_site.apps.OCLettingsSiteConfig",
    "lettings.apps.LettingsConfig",
    "profiles.apps.ProfilesConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "whitenoise.runserver_nostatic",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "oc_lettings_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "oc_lettings_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "oc-lettings-site.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# if not DEBUG:
#     STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
