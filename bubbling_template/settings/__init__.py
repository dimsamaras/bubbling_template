"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
https://dev.to/wemake-services/managing-djangos-settings-37ao
Default environment is `developement`.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'
USE_S3 = environ.get('USE_S3') == 'TRUE' or False

# ENV = 'staging'

base_settings = [
    'components/common.py',  # standard django settings
    'components/database.py',  # postgres
    'components/rq.py',  # redis and redis-queue
    'components/emails.py',  # smtp
    'components/logging.py',
    'components/firebase.py',
    'components/swagger.py',

    # You can even use glob:
    # 'components/*.py'

    # Select the right env:
    'environments/{0}.py'.format(ENV),
    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
