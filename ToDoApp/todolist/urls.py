from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('update/<todo_id>/', views.update, name='update'),
    path('delete/<todo_id>/', views.delete, name='delete'),
    path('edit<todo_id>/', views.edit, name='edit')
]