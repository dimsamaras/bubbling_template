"""
additional settings used in testing/staging
"""
import logging

import dj_database_url

from bubbling_template.settings.components.database import DATABASES

DEBUG = False

FRONTEND_HOST = 'https://bubbling.eu'

ALLOWED_HOSTS = ['bubbling-staging-common.herokuapp.com',
                 '127.0.0.1']

# will output to your console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'bubbling_firebase_authentication.authentication.FirebaseAuthenticationAnonymous',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'bubbling_firebase_authentication.firebase_anonymous_permissions.IsAuthenticatedAnonymous',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
