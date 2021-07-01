from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from dragonslayerapi.models import Roles
from rest_framework import serializers


class RoleViewSet(ViewSet):
    def list(self, request):
        statuses = Roles.objects.all()
        serializer = RoleSerializer(
            statuses, many=True, context={'request': request})
        return Response(serializer.data)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name')
