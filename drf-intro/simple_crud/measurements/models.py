from django.db import models


class DateInfo(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class Project(DateInfo):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Measurement(DateInfo):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

