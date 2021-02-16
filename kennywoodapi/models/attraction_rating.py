from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .visitor import Visitor


class AttractionRating(models.Model):

    class Meta:
        verbose_name = ("rating")
        verbose_name_plural = ("ratings")

    visitor = models.ForeignKey(
        Visitor, on_delete=models.DO_NOTHING, related_name='ratings')
    attraction = models.ForeignKey(
        "Attraction", on_delete=models.DO_NOTHING)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    note = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.rating
