from django.urls import path               # update
from .views import create_view, list_view


app_name = 'tasks'

urlpatterns = [
    path('', list_view, name='list'),
    path('create/', create_view, name='create'),
]