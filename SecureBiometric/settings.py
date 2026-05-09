"""
Django settings for SecureBiometric project.
"""

import os

# ================= BASE DIRECTORY ================= #

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ================= SECURITY ================= #

SECRET_KEY = '1x-q80%c3d&(gvgb)x+48$kfi%$3a&-phku9++z@m9nyghco%q'

DEBUG = True

ALLOWED_HOSTS = ['*']

# ================= INSTALLED APPS ================= #

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'SecureBiometricApp',
]

# ================= MIDDLEWARE ================= #

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ================= URLS ================= #

ROOT_URLCONF = 'SecureBiometric.urls'

# ================= TEMPLATES ================= #

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            os.path.join(
                BASE_DIR,
                'SecureBiometricApp',
                'templates'
            )
        ],

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

# ================= WSGI ================= #

WSGI_APPLICATION = 'SecureBiometric.wsgi.application'

# ================= DATABASE ================= #

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': os.path.join(
            BASE_DIR,
            'db.sqlite3'
        ),
    }
}

# ================= PASSWORD VALIDATION ================= #

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

# ================= LANGUAGE ================= #

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# ================= STATIC FILES ================= #

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(
    BASE_DIR,
    'staticfiles'
)

STATICFILES_DIRS = [
    os.path.join(
        BASE_DIR,
        'SecureBiometricApp',
        'static'
    ),
]

STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

# ================= DEFAULT AUTO FIELD ================= #

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
