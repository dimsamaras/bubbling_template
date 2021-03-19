import logging

DEBUG = True

FRONTEND_HOST = 'localhost'
#
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]

ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1']

TEST_RAW_PASSWORD = "drowssap_war"
TEST_EMAIL = "testuser@test.com"

# https://stackoverflow.com/questions/4558879/python-django-log-to-console-under-runserver-log-to-file-under-apache
# will output to your console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
)

INSTALLED_APPS += ['rest_framework.authtoken', ]   # noqa: F821

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'bubbling_firebase_authentication.authentication.FirebaseAuthenticationAnonymous',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
