from django.urls import path

from measurements.views import ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')

urlpatterns = router.urls
