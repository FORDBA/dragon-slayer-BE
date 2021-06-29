from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from dragonslayerapi.models import Professions
from rest_framework import serializers


class ProfessionViewSet(ViewSet):
    def list(self, request):
        statuses = Professions.objects.all()
        serializer = ProfessionSerializer(
            statuses, many=True, context={'request': request})
        return Response(serializer.data)


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        fields = ('id', 'name')
