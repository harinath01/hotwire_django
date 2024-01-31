from django.urls import path               # update
from .views import create_view

urlpatterns = [
    path('create/', create_view, name='create'),       # new
]