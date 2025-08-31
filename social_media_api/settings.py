import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# SECURITY SETTINGS
# ---------------------------
DEBUG = False  # Disable debug mode

ALLOWED_HOSTS = ['your-app-name.herokuapp.com', '127.0.0.1', 'localhost']

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True  # Only if HTTPS is enabled
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ---------------------------
# DATABASE CONFIGURATION
# ---------------------------
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://user:password@localhost:5432/dbname'
    )
}

# ---------------------------
# STATIC & MEDIA FILES
# ---------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # for collectstatic
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WhiteNoise to serve static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... rest of your middleware
]
