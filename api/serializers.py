from rest_framework import serializers

from api.models import Stand

class StandSerializer(serializers.HyperlinkedModelSerializer):
    STAND = serializers.CharField(source='stand_name')
    PWR = serializers.CharField(source='destructive_power_stat')
    SPD = serializers.CharField(source='speed_stat')
    RNG = serializers.CharField(source='range_stat')
    STA = serializers.CharField(source='stamina_stat')
    PRC = serializers.CharField(source='precision_stat')
    DEV = serializers.CharField(source='development_potential_stat')

    class Meta:
        model = Stand
        fields = [
        'id',
        'url',
        'STAND',
        # 'stand_user',
        'PWR',
        'SPD',
        'RNG',
        'STA',
        'PRC',
        'DEV',
        ]