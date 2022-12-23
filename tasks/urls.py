from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='list_task'),
    path('update/<int:id>', update, name='update_task'),
    path('delete/<int:id>', delete, name='delete_task'),
]
