from rest_framework import serializers
from .models import *


class ReactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['student','branch']
        