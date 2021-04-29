from rest_framework.serializers import ModelSerializer
from measurements.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at']
