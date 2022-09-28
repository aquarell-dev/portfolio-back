from rest_framework import serializers

from .models import Skill

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
