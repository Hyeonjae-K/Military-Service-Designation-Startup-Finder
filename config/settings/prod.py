from config.settings.__init__ import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = secret.DATABASES

STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')
