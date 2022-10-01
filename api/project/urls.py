from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectListCreate.as_view()),
    path('<int:pk>', views.ProjectDetails.as_view()),
    path('<int:project_pk>/task/', include('api.task.urls'))
]
