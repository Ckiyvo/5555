from django.urls import path
from .views import upload_files, create_project, get_projects, get_project_files, get_project_list

urlpatterns = [
    path('api/upload_files/', upload_files, name='upload_files'),
    path('api/create_project/', create_project, name='create_project'),
    path('api/get_projects/', get_projects, name='get_projects'),
    path('api/get_project_files/<str:project_name>/', get_project_files, name='get_project_files'),
    path('api/get_project_list/', get_project_list, name='get_project_list'),
]