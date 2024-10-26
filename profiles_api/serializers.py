from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    #serializes a name field
    name =serializers.CharField(max_length=10)
    #nammmm =serializers.CharField(max_length=10) #nammm/name will be present in ui