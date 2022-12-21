from rest_framework import serializers
from .models import *

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        field = ('id', 'title', 'description', 'date', 'completed')