from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from dragonslayerapi.models import Statuses
from rest_framework import serializers


class StatusViewSet(ViewSet):
    def list(self, request):
        statuses = Statuses.objects.all()
        serializer = StatusSerializer(
            statuses, many=True, context={'request': request})
        return Response(serializer.data)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ('id', 'name')
