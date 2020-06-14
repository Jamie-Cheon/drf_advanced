from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Card
        fields = '__all__'
