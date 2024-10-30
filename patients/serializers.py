from rest_framework import serializers
from .models import Partient

class PartientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partient
        fields = '__all__'