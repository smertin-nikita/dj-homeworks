from django.urls import path, register_converter

from app.views import landing, stats, index
from app.converters import LandVersionConverter

register_converter(LandVersionConverter, 'land_version')

urlpatterns = [
    path('', index, name='index'),
    path('landing/<land_version:ab_test_arg>/', landing, name='landing'),
    path('stats/', stats, name='stats'),
]
