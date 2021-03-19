
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
import os

from bubbling_template.settings.components import BASE_DIR

DB_PREFIX = 'bubbling_template_'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': os.getenv("DATABASE_NAME"),
    #     'USER': os.getenv("DATABASE_USER"),
    #     'PASSWORD': os.getenv("DATABASE_PASSWORD"),
    #     'HOST': os.getenv("DATABASE_HOST"),
    #     'PORT': os.getenv("DATABASE_PORT"),
    #     'CONN_MAX_AGE': int(os.getenv("DATABASE_CONN_MAX_AGE")),
    #     'OPTIONS': {
    #         'connect_timeout': 10,
    #     },
    # }
}
