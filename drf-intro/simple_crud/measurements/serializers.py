from rest_framework.serializers import ModelSerializer
from measurements.models import Project, Measurement
from rest_framework import fields


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at']


class MeasurementSerializer(ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'value', 'project', 'created_at', 'updated_at', 'image']

    image = fields.ImageField(allow_empty_file=True, allow_null=True, use_url=True)
