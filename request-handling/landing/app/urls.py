from django.urls import path, register_converter, re_path

from app.views import landing, stats, index


urlpatterns = [
    path('', index, name='index'),
    re_path(r'^landing/(?P<ab_test_arg>test|original)/', landing, name='landing'),
    path('stats/', stats, name='stats'),
]
