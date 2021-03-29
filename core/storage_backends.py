from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

# SUPER SIMPLE BASIC: https://blog.theodo.com/2019/07/aws-s3-upload-django/
# CHECK THIS OUT: https://medium.com/@hiteshgarg14/how-to-dynamically-select-storage-in-django-filefield-bc2e8f5883fd
# NICE ONE: https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
# VIEW PRIVATE FILES : https://www.gyford.com/phil/writing/2012/09/26/django-s3-temporary/


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    location = 'private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
