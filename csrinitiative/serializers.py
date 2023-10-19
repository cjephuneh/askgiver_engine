from rest_framework import serializers
from .models import CsrInitiative

class CsrInitiativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsrInitiative
        fields = '__all__'
