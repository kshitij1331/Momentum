from django.urls import path
from .views import home, dashboard, create_project, update_project, delete_project, project_detail, create_task, update_task, delete_task, signup_view, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('project/new/', create_project, name='create_project'),
    path('project/edit/<int:project_id>/', update_project, name='update_project'),
    path('project/delete/<int:project_id>/', delete_project, name='delete_project'),
    path('project/<int:project_id>/', project_detail, name='project_detail'),
    path('project/<int:project_id>/task/new/', create_task, name='create_task'),
    path('task/edit/<int:task_id>/', update_task, name='update_task'),
    path('task/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
