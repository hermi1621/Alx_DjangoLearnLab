INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',  # ✅ Added blog app
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Use PostgreSQL
        'NAME': 'django_blog_db',                   # Your database name
        'USER': 'your_db_user',                     # Database user
        'PASSWORD': 'your_db_password',             # Database password
        'HOST': 'localhost',                        # Usually localhost
        'PORT': '5432',                             # Default PostgreSQL port
    }
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',       # your blog app
    'taggit',     # <- this must be spelled exactly like this
]
