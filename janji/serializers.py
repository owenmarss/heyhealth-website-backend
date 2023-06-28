from rest_framework import serializers
from .models import Janji

class JanjiSerializer(serializers.ModelSerializer) :
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta :
        model = Janji
        fields = ('__all__')

class JanjiResponseSerializer(serializers.ModelSerializer) :
    user = serializers.StringRelatedField(read_only=True)
    dokter = serializers.StringRelatedField(read_only=True)

    class Meta :
        model = Janji
        fields = ('__all__')


    