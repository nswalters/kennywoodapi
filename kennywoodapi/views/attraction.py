from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from kennywoodapi.models import Attraction
from .parkarea import ParkAreaSerializer
from .attractioncategory import AttractionCategorySerializer


class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for attractions"""

    area = ParkAreaSerializer(many=False)
    category = AttractionCategorySerializer(many=False)

    class Meta:
        model = Attraction
        url = serializers.HyperlinkedIdentityField(
            view_name="attraction-detail",
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'max_occupancy',
                  'height_requirement_inches', 'area', 'category')


class AttractionViewset(ViewSet):
    """
    View for interacting with attractions
    """

    def retrieve(self, request, pk=None):
        try:
            attraction = Attraction.objects.get(pk=pk)
            serializer = AttractionSerializer(
                attraction, context={'request': request})
            return Response(serializer.data)

        except Attraction.DoesNotExist as ex:
            return Response(
                {'message': "The requested attraction does not exist, or you do not have permission to access it"},
                status=status.HTTP_404_NOT_FOUND
            )

    def list(self, request):
        attractions = Attraction.objects.all()

        json_attractions = AttractionSerializer(
            attractions, many=True, context={'request': request}
        )

        return Response(json_attractions.data)
