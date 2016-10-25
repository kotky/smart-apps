from rest_framework import serializers
from .models import UniversalJsonContainer


class UniversalJsonContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversalJsonContainer
        fields = ('id','session_id', 'content_type', 'data')