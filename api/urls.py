from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path('users/', include('users.urls'), name="user"),
    path('vlogs/', include('vlogs.urls'), name="vlog"),
    path('projects/', include('projects.urls'), name="project"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
