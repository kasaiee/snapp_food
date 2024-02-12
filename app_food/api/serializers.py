from app_food.models import Food
from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.__class__.__name__.lower()


class FoodSearchSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Food
        fields = ['title']


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    restaurant_title = serializers.SerializerMethodField()

    def get_restaurant_title(self, obj):
        return obj.restaurant.title
    
    subtotal = serializers.SerializerMethodField()

    def get_subtotal(self, obj):
        return obj.price * (1 - obj.discount / 100)
    
    class Meta:
        model = Food
        fields = [
            'title',
            'restaurant_title',
            'price',
            'discount',
            'subtotal',
            'image'
        ]