from rest_framework import serializers

from kennywoodapi.models import TargetPopulation


class TargetPopulationSerializer(serializers.ModelSerializer):
    """
    JSON serializer for target population data
    """
    class Meta:
        model = TargetPopulation
        fields = ('id', 'name')
        depth = 1
