from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/', views.dummy_view, name='task_update_no_id'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
    path('delete/', views.dummy_view, name='task_delete_no_id'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    ]
