from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hash', views.hash_service, name='hash'),
    path('request_log', views.request_log, name='request_log')
]