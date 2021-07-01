from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from dragonslayerapi.models import Ranks
from rest_framework import serializers


class RankViewSet(ViewSet):
    def list(self, request):
        statuses = Ranks.objects.all()
        serializer = RankSerializer(
            statuses, many=True, context={'request': request})
        return Response(serializer.data)


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranks
        fields = ('id', 'name')
