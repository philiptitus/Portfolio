from .settings import *  # Import everything from your existing settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to your SQLite database
    }
}
