
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

SECRET_KEY = 'notsecure'

INSTALLED_APPS = (
    'security_middleware',
)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

ROOT_URLCONF = 'urls'

MIDDLEWARE_CLASSES = (
    'security_middleware.middleware.SSLMiddleware',
    'security_middleware.middleware.ContentSecurityPolicyMiddleware',
    'security_middleware.middleware.XSSProtectionMiddleware',
    'security_middleware.middleware.NoSniffMiddleware',
)
