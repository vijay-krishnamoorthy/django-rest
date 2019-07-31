import rest_framework
from rest_framework import serializers
from .models import Plan

class Planserializer(serializers.Serializer):
    pk=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    price = serializers.IntegerField()
    validity = serializers.IntegerField()
    description = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        return Plan.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.price=validated_data.get('price', instance.price)
        instance.validity=validated_data.get('validity', instance.validity)
        instance.description=validated_data.get('description', instance.description)
        instance.save()
        return instance

