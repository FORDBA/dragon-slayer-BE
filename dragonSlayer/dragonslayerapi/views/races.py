from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from dragonslayerapi.models import Races
from rest_framework import serializers


class RaceViewSet(ViewSet):
    def list(self, request):
        statuses = Races.objects.all()
        serializer = RaceSerializer(
            statuses, many=True, context={'request': request})
        return Response(serializer.data)


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Races
        fields = ('id', 'name')
