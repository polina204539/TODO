from rest_framework import serializers
from .models import Todolist

class TodoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todolist
        fields = '__all__'

    def create(self, validated_data):
        return Todolist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.description = validated_data.get("description", instance.description)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance

