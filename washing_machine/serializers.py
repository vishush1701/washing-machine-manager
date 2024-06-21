from rest_framework import serializers
from .models import WashingMachine,Location,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','location']
        depth = 1

class WashingMachineSerializer(serializers.ModelSerializer):
    using_by = UserSerializer(required=False)

    class Meta:
        model = WashingMachine
        fields = ['id','name','is_available','location','using_by']
        depth = 2

    def update(self, instance, validated_data):
        if instance.is_available:
            name = validated_data.get('using_by').get('name')
            user = User.objects.get(name=name)
            instance.using_by = user
            instance.is_available = False
            instance.save()
        return instance

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id','building_name','floor','room']

