from django.urls import path

from . import views

app_name = 'emailer'
urlpatterns = [
        path('', views.index, name='index'),
        ]
