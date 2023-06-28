from rest_framework import serializers
from .models import Rs


class RsSerializer(serializers.ModelSerializer) :
    class Meta :
        model=Rs  
        fields=('__all__')

class RsNamaSerializer(serializers.ModelSerializer) :
    class Meta :
        model=Rs
        fields=['nama']