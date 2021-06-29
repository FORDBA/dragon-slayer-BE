from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from dragonslayerapi.models import PlayerClasses
from rest_framework import serializers


class PlayerClassViewSet(ViewSet):
    def list(self, request):
        statuses = PlayerClasses.objects.all()
        serializer = PlayerClassSerializer(
            statuses, many=True, context={'request': request})
        return Response(serializer.data)


class PlayerClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerClasses
        fields = ('id', 'name')
