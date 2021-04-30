from rest_framework.serializers import ModelSerializer
from measurements.models import Project, Measurement


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at']


class MeasurementSerializer(ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'value', 'project', 'created_at', 'updated_at']
