from django.db import models
from .attraction_rating import AttractionRating
from .attraction_category import AttractionCategory
from .park_area import ParkArea


class Attraction(models.Model):

    class Meta:
        verbose_name = ("attraction")
        verbose_name_plural = ("attractions")

    name = models.CharField(max_length=100)
    area = models.ForeignKey(
        ParkArea, on_delete=models.DO_NOTHING, related_name='attractions')
    category = models.ForeignKey(
        AttractionCategory, on_delete=models.DO_NOTHING, related_name='attractions')
    max_occupancy = models.IntegerField(null=True)
    height_requirement_inches = models.IntegerField(null=True)

    @property
    def can_be_rated(self):
        """
        can_be_rated property, caluclated per user

        Returns:
            boolean -- If the user can rate the product or not
        """

        return self.__can_be_rated

    @can_be_rated.setter
    def can_be_rated(self, value):
        self.__can_be_rated = value

    @property
    def average_rating(self):
        """
        Average rating calculated for each attraction

        Returns:
            number -- The average rating for the attraction
        """
        ratings = AttractionRating.objects.filter(attraction=self)
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating

        # If there are no rating, then we set the average to 0
        # otherwise we calculate the average
        try:
            avg = total_rating / len(ratings)
        except ZeroDivisionError:
            avg = total_rating

        return avg
