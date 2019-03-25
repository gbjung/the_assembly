from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEV = True
MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
INSTALLED_APPS += (
    'debug_toolbar',
)
INTERNAL_IPS = ('127.0.0.1', )
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")
ANYMAIL = {
    "SENDGRID_API_KEY": env("SENDGRID_API_KEY"),
    "SENDGRID_API_URL": env("SENDGRID_API_URL")
}
MAILCHIMP_KEY = env("MAILCHIMP_KEY")
MAILCHIMP_USER = env("MAILCHIMP_USER")
MAILCHIMP_LIST_ID = env("MAILCHIMP_LIST_ID")
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    from .local import *
except ImportError:
    pass
