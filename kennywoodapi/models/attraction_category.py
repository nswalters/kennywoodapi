from django.db import models


class AttractionCategory(models.Model):

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
