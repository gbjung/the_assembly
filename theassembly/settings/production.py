from .base import *
import netifaces

DEBUG = False

def ip_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        for x in (netifaces.AF_INET, netifaces.AF_INET6):
            if x in addrs:
                ip_list.append(addrs[x][0]['addr'])
    return ip_list

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ip_addresses()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env("EMAIL_PORT")

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
