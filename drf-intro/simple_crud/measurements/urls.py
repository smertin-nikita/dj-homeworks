from django.urls import path

from measurements.views import ProjectViewSet, MeasurementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('measurements', MeasurementViewSet, basename='measurements')

urlpatterns = router.urls
