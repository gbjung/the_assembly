from .base import *

DEV = False
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")

AWS_S3_REGION_NAME = env("DO_REGION")
AWS_S3_ENDPOINT_URL = env("DO_ENDPOINT")
AWS_ACCESS_KEY_ID = env("DO_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = env("DO_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = env("DO_BUCKET_NAME")
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}
try:
    from .local import *
except ImportError:
    pass
