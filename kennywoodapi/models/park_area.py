from django.db import models
from .target_population import TargetPopulation


class ParkArea(models.Model):

    class Meta:
        verbose_name = ("area")
        verbose_name_plural = ("areas")

    name = models.CharField(max_length=50)
    target_population = models.ForeignKey(
        TargetPopulation, on_delete=models.DO_NOTHING)
