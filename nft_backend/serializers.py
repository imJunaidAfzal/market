from rest_framework import serializers
from .models import *


class BidingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biding
        fields = "__all__"