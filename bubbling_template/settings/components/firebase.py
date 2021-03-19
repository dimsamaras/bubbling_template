import os

FIREBASE_API_KEY = os.getenv('FIREBASE_API_KEY')

# Can also implement this way with dick instead of cert file.
# FIREBASE_CREDENTIALS = {
#     "type": "service_account",
#     "project_id": os.getenv('FIREBASE_PROJECT_ID'),
#     "private_key_id": os.getenv('FIREBASE_PRIVATE_KEY_ID'),
#     "private_key": os.getenv('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
#     "client_email": os.getenv('FIREBASE_CLIENT_EMAIL'),
#     "client_id": os.getenv('FIREBASE_CLIENT_ID'),
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://accounts.google.com/o/oauth2/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": os.getenv('FIREBASE_CLIENT_CERT_URL')
# }
