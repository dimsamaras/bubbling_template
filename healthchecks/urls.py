from django.urls import path

from . import views

urlpatterns = [
    path('service/', views.index, name='server'),
    path('db/', views.database, name='database')
]
