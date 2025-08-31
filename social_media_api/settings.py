# social_media_api/settings.py

# Turn off debug mode for production
DEBUG = False

# Add your domain(s) or Heroku app URL
ALLOWED_HOSTS = ['your-app-name.herokuapp.com', '127.0.0.1', 'localhost']

# Optional: if using PostgreSQL on Heroku
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='postgres://user:password@localhost:5432/dbname')
}
