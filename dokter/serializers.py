from rest_framework import serializers

from rumah_sakit.serializers import RsNamaSerializer
from .models import Dokter


class DokterSerializer(serializers.ModelSerializer):
    lokasi_praktek = RsNamaSerializer(read_only=True)

    class Meta:
        model=Dokter  
        fields=('__all__')