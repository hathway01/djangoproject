from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('project.urls')),
    path('project/', include('project.urls')),
    path('admin/', admin.site.urls),
]
