from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('filter/<str:priority>/', views.task_filter, name='task_filter'),
]
