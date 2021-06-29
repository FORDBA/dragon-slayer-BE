from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from dragonslayerapi.models import Dungeons
from rest_framework import serializers


class DungeonViewSet(ViewSet):
    def list(self, request):
        statuses = Dungeons.objects.all()
        serializer = DungeonSerializer(
            statuses, many=True, context={'request': request})
        return Response(serializer.data)


class DungeonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dungeons
        fields = ('id', 'name')
