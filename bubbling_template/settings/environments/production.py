"""
additional settings used in production
"""
import logging
import os

DEBUG = False

ALLOWED_HOSTS = ['']

FRONTEND_HOST = '******'

# For django storages
# AZURE_ACCOUNT_NAME = "******"
# AZURE_ACCOUNT_KEY = "******"
# AZURE_CONTAINER = "******"
# SHARE_URL = "******"
# AZURE_BLOB_CUSTOM_DOMAIN = "******"
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = '******'
# STATIC_URL = "https://%s/%s/" % (AZURE_BLOB_CUSTOM_DOMAIN,
#                                  STATICFILES_LOCATION)
# MEDIAFILES_LOCATION = 'mediafiles'
# DEFAULT_FILE_STORAGE = '******'
# MEDIA_URL = "https://%s/%s/" % (AZURE_BLOB_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='/server_logs.log',
    filemode='a'
)

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
