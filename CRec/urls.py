from django.urls import path

from . import views

app_name = 'CRec'
urlpatterns = [
    path('', views.index, name='index')
]
