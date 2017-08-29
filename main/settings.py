"""
Django settings for sdi_api project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pf1&!nhd&i4p=r%aa@m!1r#r^6v*ncl@hkhg6a22mj@o8j+-ty'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
        'localhost', '127.0.0.1', '.speculoos'
        ]

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'layers',
    'api',
    'clients',
    'rest_framework',
    'rest_framework_gis',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'main/templates'),
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'PORT': 5433,
        'NAME': 'django',
        'PASSWORD': 'plokplok',
        'USER': 'pierre',
    },

    'layers': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': '10.99.99.11',
        'NAME': 'tev',
        'PASSWORD': 'poireau',
        'USER': 'pacome',
        'OPTIONS': {
            'options': '-c search_path=tev,david,public',
        }
    }
}

LAYERS_DB = {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'HOST': '10.99.99.11',
    'NAME': 'tev',
    'PASSWORD': 'poireau',
    'USER': 'pacome',
}
LAYERS_SCHEMAS = [
    'tev',
    'david',
]

for schema in LAYERS_SCHEMAS:
    db_config = LAYERS_DB.copy()
    db_config.update({
        'OPTIONS': {
            'options': '-c search_path={},public'.format(schema),
        },
    })
    DATABASES[schema] = db_config


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


CLIENTS = {
    'edit': '/home/pierre/System/src/be-sdi/sdi-webgis-rw/dist',
}

DEFAULT_BASE_LAYER = {
    'name': {
        'fr': 'urbisFRGray',
        'nl': 'urbisNLGray',
    },
    'srs': 'EPSG:31370',
    'params': {
        'LAYERS': {
            'fr': 'urbisFRGray',
            'nl': 'urbisNLGray',
        },
        'VERSION': '1.1.1',
    },
    'url': {
        'fr': 'https://geoservices-urbis.irisnet.be/geoserver/ows',
        'nl': 'https://geoservices-urbis.irisnet.be/geoserver/ows',
    },
}
