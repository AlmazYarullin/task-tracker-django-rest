from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListCreate.as_view()),
    path('<int:pk>', views.ProjectDetails.as_view())
]
