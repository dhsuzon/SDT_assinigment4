
from django.contrib import admin
from django.urls import path,include
from .views import Taskview,Task_edit,Task_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include("category.urls")),
    path('task/', include("task.urls")),
    path('',Taskview,name="task_show"),
    path('edit/<int:id>/',Task_edit,name="task_edit"),
    path('delete/<int:id>/',Task_delete,name="task_delete"),
]
