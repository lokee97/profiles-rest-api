from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    #serializes a name field
    name =serializers.CharField(max_length=10)
    #nammmm =serializers.CharField(max_length=10) #nammm/name will be present in ui


class UserProfileSerializer(serializers.ModelSerializer):
    #Serializers a user profile object
    class Meta:
        model = models.userProfile
        fields=('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type': 'password'}
            }
        }
    
    def create(self,validated_data):
        #create and returns a new user
        user = models.userProfile.objects.create_user(
        email = validated_data['email'],
        name = validated_data['name'],
        password = validated_data['password']
        )
        return user
    
    def update(self,instance,validated_data):
        #Handle updating user account
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance,validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    #Serializers profile feed items

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}  # user_profile is set to read_only because only the authenticated user can add feeds to that profile....we can avoid unnecessary creation of profiles and feeds
