from django.db import models


class TargetPopulation(models.Model):

    class Meta:
        verbose_name = ("population")
        verbose_name_plural = ("populations")

    name = models.CharField(max_length=50)
