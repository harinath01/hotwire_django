from django.urls import path               # update
from .views import create_view, list_view, update_view, detail_view, delete_view


app_name = 'tasks'

urlpatterns = [
    path('', list_view, name='list'),
    path('create/', create_view, name='create'),
    path('<int:pk>/', detail_view, name='detail'),
    path('<int:pk>/delete', delete_view, name='delete'),
    path('<int:pk>/update/', update_view, name='update'),
]