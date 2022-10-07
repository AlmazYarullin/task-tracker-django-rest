from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('api.project.urls')),
    path('user/', include('api.user.urls'))
]
