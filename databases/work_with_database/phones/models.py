from django.db import models


class Phone(models.Model):
    name = models.TextField()
    image = models.URLField()
    price = models.IntegerField()
    date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)
