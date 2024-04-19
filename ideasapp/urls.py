from django.urls import path
from . import views

urlpatterns = [
    path('', views.ideas_list, name='ideas_list'),
    path('create/', views.create_idea, name='create_idea'),
    path('edit/<int:pk>/', views.edit_idea, name='edit_idea'),
    path('delete/<int:pk>/', views.delete_idea, name='delete_idea'),
]
