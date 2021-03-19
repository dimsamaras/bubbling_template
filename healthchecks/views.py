from django.http import HttpResponse
from django.db import connection


def index(request):
    return HttpResponse("ok")


def database(request):
    with connection.cursor() as cursor:
        cursor.execute("select 1")
        one = cursor.fetchone()[0]
        if one != 1:
            raise Exception('The db health check failed')
    return HttpResponse("ok")
