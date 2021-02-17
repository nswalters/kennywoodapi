from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from kennywoodapi.models import ParkArea
from .targetpopulation import TargetPopulationSerializer


class ParkAreaSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for park areas"""

    target_population = TargetPopulationSerializer(many=False)

    class Meta:
        model = ParkArea
        url = serializers.HyperlinkedIdentityField(
            view_name='parkarea-detail',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'target_population')
        depth = 2


class ParkAreaViewset(ViewSet):
    """
    View for interacting with park areas
    """

    def retrieve(self, request, pk=None):
        try:
            area = ParkArea.objects.get(pk=pk)
            serializer = ParkAreaSerializer(area, context={'request': request})
            return Response(serializer.data)

        except ParkArea.DoesNotExist as ex:
            return Response(
                {'message': "The requested park area does not exist, or you do not have permission to access it"},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        areas = ParkArea.objects.all()

        json_areas = ParkAreaSerializer(
            areas, many=True, context={'request': request}
        )

        return Response(json_areas.data)
