from django.urls import path
from task.views import  add_task

urlpatterns = [
   
    path('add/',add_task,name="add_task"),
]