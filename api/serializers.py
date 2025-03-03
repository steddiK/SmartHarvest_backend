from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ZonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zones
        fields = '__all__'

class PlantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantes
        fields = '__all__'

class DiagnosticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostics
        fields = '__all__'

class RecommandationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommandations
        fields = '__all__'
