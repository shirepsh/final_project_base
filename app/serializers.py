from rest_framework import serializers
from .models import  *

#category model serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ( "__all__")

#product model serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( "__all__")

#cart model serializers
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ( "__all__")

    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Order.objects.create(**validated_data, user=user)

#profile model serializers
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ( "__all__")

    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Profile.objects.create(**validated_data, user=user)
