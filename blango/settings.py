"""
Django settings for blango project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

import dj_database_url
from configurations import Configuration, values


class Dev(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

    SECRET_KEY = "django-insecure-+sn%dpa!086+g+%44z9*^j^q-u4n!j(#wl)x9a%_1op@zz2+1-"

    DEBUG = values.BooleanValue(True)

    ALLOWED_HOSTS = values.ListValue(["127.0.0.1", "localhost"])

    SITE_ID = 1

    # Application definition

    INSTALLED_APPS = [
        "blango_auth",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.sites",
        "django.contrib.sitemaps",
        "django.contrib.staticfiles",
        "blog",
        "crispy_forms",
        "crispy_bootstrap5",
        "debug_toolbar",
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "allauth.socialaccount.providers.google",
        "rest_framework",
        "rest_framework.authtoken",
        "drf_yasg",
        "django_filters",
        "versatileimagefield",
        "corsheaders",
        "markdownify.apps.MarkdownifyConfig",
    ]

    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "blango.urls"

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

    WSGI_APPLICATION = "blango.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    # DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3")
    DATABASES = {
        "default": dj_database_url.config(default=f"sqlite:///{BASE_DIR}/db.sqlite3"),
        "alternative": dj_database_url.config(
            "ALTERNATIVE_DATABASE_URL",
            default=f"sqlite:///{BASE_DIR}/alternative_db.sqlite3",
        ),
    }

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.BasicAuthentication",
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.TokenAuthentication",
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ],
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.IsAuthenticatedOrReadOnly"
        ],
        "DEFAULT_THROTTLE_CLASSES": [
            "blog.api.throttling.AnonSustainedThrottle",
            "blog.api.throttling.AnonBurstThrottle",
            "blog.api.throttling.UserSustainedThrottle",
            "blog.api.throttling.UserBurstThrottle",
        ],
        "DEFAULT_THROTTLE_RATES": {
            "anon_sustained": "500/day",
            "anon_burst": "10/minute",
            "user_sustained": "5000/day",
            "user_burst": "100/minute",
        },
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 100,
        "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend",
            "rest_framework.filters.OrderingFilter",
        ],
    }

    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = values.Value("UTC")

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = "/static/"

    STATIC_ROOT = BASE_DIR / "static"

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse",
            },
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            },
        },
        "formatters": {
            "rich": {"datefmt": "[%X]"},
        },
        "handlers": {
            "console": {
                "class": "rich.logging.RichHandler",
                "filters": ["require_debug_true"],
                "formatter": "rich",
                "level": "DEBUG",
                "rich_tracebacks": True,
                "tracebacks_show_locals": True,
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
                "filters": ["require_debug_false"],
            },
        },
        "loggers": {
            "django.request": {
                "handlers": ["mail_admins"],
                "level": "ERROR",
                "propagate": True,
            },
            "django": {
                "handlers": [],
                "level": "INFO",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "INFO",
        },
    }

    PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.Argon2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
        "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    ]

    INTERNAL_IPS = []

    AUTH_USER_MODEL = "blango_auth.User"

    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    ACCOUNT_ACTIVATION_DAYS = 7

    SITE_ID = 1
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = "email"

    SWAGGER_SETTINGS = {
        "SECURITY_DEFINITIONS": {
            "Token": {"type": "apiKey", "name": "Authorization", "in": "header"},
            "Basic": {"type": "basic"},
        }
    }

    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    }

    MEDIA_ROOT = BASE_DIR / "media"
    MEDIA_URL = "/media/"

    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)

    MARKDOWNIFY = {
        "default": {
            "MARKDOWN_EXTENSIONS": [
                "markdown.extensions.extra",  # This includes fenced code, and others
                "markdown.extensions.codehilite",
            ],
            "WHITELIST_TAGS": [
                "img",
                "p",
                "blockquote",
                "ol",
                "li",
                "ul",
                "a",
                "em",
                "strong",
                "h3",
                "mark",
                "code",
                "pre",
                "span",
                "div",
            ],
            "WHITELIST_ATTRS": [
                "class",
                "href",
                "src",
            ],
            "BLEACH": True,
        }
    }

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

    CRISPY_TEMPLATE_PACK = "bootstrap5"


class Prod(Dev):
    DEBUG = False
    SECRET_KEY = values.SecretValue()
    ALLOWED_HOSTS = values.ListValue(["www.eduardoargueta.me"])
    STATIC_ROOT = "/home/weaponx/blango/static"
