from django.contrib import admin
from django.urls import path
from .views import task_list, my_view, delete_task, complete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),  
    path('update-task/', my_view, name='update_task'),  
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),  
    path('complete-task/<int:task_id>/', complete_task, name='complete_task'),  
]
