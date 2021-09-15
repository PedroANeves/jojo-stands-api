from rest_framework import serializers

from api.models import Stand

class StandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stand
        fields = ['id', 'url', 'stand_name', 'stand_user']