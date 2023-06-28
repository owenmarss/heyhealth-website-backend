from rest_framework import serializers
from .models import Penyakit

class PenyakitSerializer(serializers.ModelSerializer) :
    class Meta:
        model=Penyakit
        fields=('__all__')