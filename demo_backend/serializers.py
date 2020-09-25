from rest_framework import serializers
from .models import userData

class userSerializer(serializers.ModelSerializer):
    class Meta :
        model = userData
        fields = '__all__'