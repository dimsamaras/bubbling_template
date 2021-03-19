import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
SENDER_EMAIL = 'info@bubbling.eu'
SENDER_NAME = 'The bubbling team'
