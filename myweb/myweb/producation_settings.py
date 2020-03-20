# import all default settings
from .settings import *

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

# Static asset configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS=(
("images",os.path.join(STATIC_ROOT,'images').replace('\\','/')),
("css",os.path.join(STATIC_ROOT,'css').replace('\\','/')),
("js",os.path.join(STATIC_ROOT,'js').replace('\\','/')),
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode
DEBUG = False

TEMPLATE_DEBUG = False
