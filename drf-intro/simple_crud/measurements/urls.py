from django.urls import path

from measurements.views import ProjectViewSet, MeasurementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register('values', MeasurementViewSet, basename='measurement')

urlpatterns = router.urls
