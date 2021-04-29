from django.contrib import admin

from measurements.models import Project, Measurement

admin.site.register(Project)
admin.site.register(Measurement)
