
#EXTERNAL COMPONENTS

## FIREBASE
Use firebase authentication with your django rest framework project

On your project's `settings.py` add this to the `REST_FRAMEWORK` configuration

```python
REST_FRAMEWORK = {
    ...
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "firebase_auth.authentication.FirebaseAuthentication"
    ]
    ...
}
```

Get your admin credentials `.json` from the Firebase SDK and add them to your project in `user_operator/settings` folder named as `firebase-cert.json`!

Get your web api key and add it to your local .env file.

```python
FIREBASE_AUTH = {
    "SERVICE_ACCOUNT_KEY_FILE" =  BASE_DIR.joinpath("./user_operator/settings/firebase-cert.json").__str__(), # your firebase ceritification file
}
```
else
use the `"SERVICE_ACCOUNT_KEY_FILE" ` dict in `common.py` to set firebase-cert as env variables!

The `django-rest-firebase-auth` comes with the following settings as default, which can be overridden in your project's `settings.py`.

```python
FIREBASE_AUTH = {
    "SERVICE_ACCOUNT_KEY_FILE": "",

    # require that user has verified their email
    "EMAIL_VERIFICATION": False
}
```
