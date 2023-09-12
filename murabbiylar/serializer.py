from rest_framework import serializers
from .models import TrenerModel


class TrenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrenerModel
        fields = "__all__"
