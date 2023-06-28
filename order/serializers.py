from rest_framework import serializers
from .models import Order
from item.serializers import ItemNamaSerializer,ItemSerializer
from item.models import Item

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model=Order
        fields=('user', 'items', 'quantities', 'alamat', 'nomor_telepon', 'pembayaran')
        # fields=('__all__')

    def create(self,validated_data) :
        extra_items = validated_data.pop('items')
        extra_items = [Item.objects.get(id=item_id) for item_id in extra_items]

        # items_id = validated_data.pop('items')
        # items = Item.objects.filter(id__in=items_id)
        order = Order.objects.create(**validated_data)
        order.items.set(extra_items)
        order.save()
        return order

class OrderResponseSerializer(serializers.ModelSerializer) :
    items = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta :
        model = Order
        fields = ('user', 'items', 'quantities', 'alamat', 'nomor_telepon', 'pembayaran')

    def get_items(self,obj) :
        return [item.nama for item in obj.items.all()]