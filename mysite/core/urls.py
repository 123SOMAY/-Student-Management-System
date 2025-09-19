from django.urls import path
from . import views

urlpatterns = [
    # Todo URLs
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/add/', views.add_todo, name='add_todo'),
    path('todos/toggle/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('todos/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    
    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Student Management URLs
    path('', views.student_list, name='student_list'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/edit/<int:student_id>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:student_id>/', views.student_delete, name='student_delete'),
]