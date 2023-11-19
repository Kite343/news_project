"""
Django settings for city_newsproject project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^ob$x8y&khu)01)zf(fv^#a65nh+f#m0)bimw9xa7&&_3gg+36'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['192.168.0.167',
                 '127.0.0.1',
                 ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newsapp.apps.NewsappConfig',
    'forum_app.apps.ForumAppConfig',
    "users.apps.UsersConfig",
    'captcha',
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

ROOT_URLCONF = 'city_newsproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
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

WSGI_APPLICATION = 'city_newsproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'users:login'

AUTH_USER_MODEL = 'users.User'

LOGGING = {'version': 1,
           'disable_existing_loggers': False,
           # форматы логирования
           'formatters': {
               # обычное форматирование
               'simple': {
                   # Добавляет вывод уровня предупреждения и само сообщение
                   'format': '%(levelname)s %(message)s'
               },
               # более крутое форматирование
               'verbose': {
                   'format': '{levelname} {asctime} {module} {process} {thread} {message}',
                   # стиль строки форматирования - фигурные скобки
                   'style': '{',
               },
           },
           # обработчики логирования
           'handlers': {
               # логирование в консоль
               'console': {
                   'class': 'logging.StreamHandler',
                   'formatter': 'verbose', # добавлен параметр formatter
               },
               # логирование в файл
               'file': {
                   'class': 'logging.FileHandler',
                   # 'filename': '/path/to/django.log',
                   'filename': './log/django.log',
                   'formatter': 'verbose', # добавлен параметр formatter
                   'level': 'INFO',
               },
           },
           'loggers': {
               # логирование всего django-сервера
               'django': {
                   # обработчики логирования (оба)
                    'handlers': ['console', 'file'],
                   'level': 'INFO',
                    # 'level': 'WARNING',
               },
                'newsapp': {
                   # обработчик - только консоль
                   # 'handlers': ['console'],
                   # обработчик - консоль и файл
                    'handlers': ['console', 'file'],
                #    'level': 'DEBUG',
                   'level': 'INFO',
                    # 'level': 'WARNING',
                   # если есть более вышестоящие логгеры, то их тоже используем
                    'propagate': True,
               },
                'forum_app': {
                   # обработчик - только консоль
                   # 'handlers': ['console'],
                   # обработчик - консоль и файл
                    'handlers': ['console', 'file'],
                #    'level': 'DEBUG',
                #    'level': 'INFO',
                    'level': 'WARNING',
                   # если есть более вышестоящие логгеры, то их тоже используем
                    'propagate': True,
               }, 
                'users': {
                   # обработчик - только консоль
                   # 'handlers': ['console'],
                   # обработчик - консоль и файл
                    'handlers': ['console', 'file'],
                #    'level': 'DEBUG',
                #    'level': 'INFO',
                    'level': 'WARNING',
                   # если есть более вышестоящие логгеры, то их тоже используем
                    'propagate': True,
               },           
           },
           }


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'city_newsproject_cache'),
    }
}