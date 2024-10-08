"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

URL_PREFIX = "backend"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/" + URL_PREFIX + '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "/" + URL_PREFIX + '/static/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', "django-insecure-va=jrmk350#&^7a$gan2&v5#(m8r8$5gp(0dx52g7%8h4cb51p")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG_BACKEND')=="true")

ALLOWED_HOSTS = [
    f"{os.getenv('FRONTEND_HOST')}", # only if backend and frontend are hosted on the same domain. FRONTEND_HOST here means "example.com"
    os.getenv('BACKEND_HOST'),
    "0.0.0.0",
    "127.0.0.1",
    "localhost",
    "backend",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local
    'clients',
    'core',
    'events',
    'house_reservations',
    'house_reservations_billing',
    'house_reservations_management',
    'houses',
    'additional_services',

    # 3-rd party
    'corsheaders',
    'cachalot',
    'django_admin_listfilter_dropdown',
    'rest_framework',
    'django_celery_beat',
    'django_celery_results',
]

MIDDLEWARE = [
#    'core.middleware.DebugMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    f"https://{os.getenv('FRONTEND_HOST')}",
    f"http://{os.getenv('FRONTEND_HOST')}",
    f"http://{os.getenv('FRONTEND_HOST')}:80",
    f"http://{os.getenv('FRONTEND_HOST')}:3000",
    "http://127.0.0.1",
    "http://localhost",
    "http://0.0.0.0",
    "http://127.0.0.1:80",
    "http://localhost:80",
    "http://0.0.0.0:80",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://0.0.0.0:3000",
]

CSRF_TRUSTED_ORIGINS = [
    f"https://{os.getenv('FRONTEND_HOST')}",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', "postgres"),
        'USER': os.getenv('POSTGRES_USER', "postgres"),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', "postgres"),
        'HOST': os.getenv('POSTGRES_HOST', "localhost"),
        'PORT': os.getenv('POSTGRES_PORT', "5432"),
    }
}
_REDIS_URL=f"redis://{os.getenv('REDIS_USERNAME')}:{os.getenv('REDIS_PASSWORD')}@{os.getenv('REDIS_HOST', 'localhost')}:{os.getenv('REDIS_PORT', '6379')}"

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        # Строчка выше нужна для авторизации в браузерной версии апи.
        # То же самое с группой url'ов api-auth
        'rest_framework.authentication.BasicAuthentication',
    ],
    'EXCEPTION_HANDLER': 'core.middleware.custom_exceptions_handler'
}

CACHALOT_ENABLED = (os.getenv('ENABLE_CACHALOT') == "true")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"{_REDIS_URL}/0",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True
DATETIME_INPUT_FORMATS = [
    "%d-%m-%Y %H:%M:%S",
    "%d-%m-%Y %H:%M:%S.%f",
    "%d-%m-%Y %H:%M",
    "%d/%m/%Y %H:%M:%S",
    "%d/%m/%Y %H:%M:%S.%f",
    "%d/%m/%Y %H:%M",
    "%d/%m/%Y %H:%M:%S",
    "%d/%m/%Y %H:%M:%S.%f",
    "%d/%m/%Y %H:%M",
    "%d-%m-%YT%H:%M:%S",
    "%d-%m-%YT%H:%M:%S.%f",
    "%d-%m-%YT%H:%M",
    "%d/%m/%YT%H:%M:%S",
    "%d/%m/%YT%H:%M:%S.%f",
    "%d/%m/%YT%H:%M",
    "%d/%m/%YT%H:%M:%S",
    "%d/%m/%YT%H:%M:%S.%f",
    "%d/%m/%YT%H:%M",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# создание файла для записи логов, если его не существует
if not os.path.exists(os.path.join(BASE_DIR, "logs", "log.log")):
    if not os.path.exists(os.path.join(BASE_DIR, "logs")):
        os.mkdir(os.path.join(BASE_DIR, "logs"))
    with open(os.path.join(BASE_DIR, "logs", "log.log"), 'w', encoding='utf-8'):
        pass

LOGGING = {
    'version': 1,
    "disable_existing_loggers": False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(funcName)s  %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'rotating_file_handler': {
            'level': 'WARNING',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/log.log',
            'mode': 'w',
            'maxBytes': 1048576,
            'backupCount': 10
        },
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'rotating_file_handler'],
        },
        'django.db.backends': {
            'level': 'WARNING',
            'handlers': ['console', 'rotating_file_handler'],
            "propagate": False,  # чтобы не дублировалось в консоли
        }
    }
}

# Celery Configuration Options
CELERY_TIMEZONE = "Europe/Moscow"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_CACHE_BACKEND = 'django-cache'
CELERY_BROKER_URL = f"{_REDIS_URL}/1"
CELERY_RESULT_BACKEND = f"{_REDIS_URL}/1"
