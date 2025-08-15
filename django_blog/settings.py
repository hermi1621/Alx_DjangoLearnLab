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

