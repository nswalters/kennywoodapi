from rest_framework import serializers

from kennywoodapi.models import AttractionCategory


class AttractionCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for attraction categories"""

    class Meta:
        model = AttractionCategory
        url = serializers.HyperlinkedIdentityField(
            view_name="attractioncategory-detail",
            lookup_field='id'
        )
        fields = ('id', 'name', 'description')
