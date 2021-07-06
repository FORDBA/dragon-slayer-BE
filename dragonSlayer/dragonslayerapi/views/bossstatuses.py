from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from dragonslayerapi.models import BossStatuses
from rest_framework import serializers



class BossStatusViewSet(ViewSet):
    def list(self, request):
        Bossstatuses = BossStatuses.objects.all()
        serializer = BossStatusSerializer(
            Bossstatuses, many=True, context={'request': request})
        return Response(serializer.data)


class BossStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BossStatuses
        fields = ('id', 'name')
