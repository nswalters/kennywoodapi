from django.db import models
from .visitor import Visitor
from .attraction import Attraction


class Itinerary(models.Model):

    class Meta:
        verbose_name = ("itinerary")
        verbose_name_plural = ("itineraries")

    visitor = models.ForeignKey(
        Visitor, on_delete=models.DO_NOTHING, related_name='itinerary')
    attraction = models.ForeignKey(
        Attraction, on_delete=models.DO_NOTHING, related_name='itenerary')
    time = models.DateTimeField()
