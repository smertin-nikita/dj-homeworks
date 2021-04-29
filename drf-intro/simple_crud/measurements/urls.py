from django.urls import path

from measurements.views import ProjectViewSet

urlpatterns = [
    path('v1/projects/', ProjectViewSet.as_view(), name='projects')
]
