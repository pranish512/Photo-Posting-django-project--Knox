import json
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# TO GET NEST DATA:::::
class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        password = make_password(validated_data['password'])
        )
        # user.set_password(validated_data['password'])
        # user.save()
        return user
    
        # password = make_password(validated_data['password'])

    # def create(self, validated_data):
    #     return super().create_user(**validated_data)

    def get_username(self, name):
        name = User.objects.filter(username=name)
        if name.exists():
            raise serializers.ValidationError('Username is already taken!!!')
        return name

class EntryPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser']

class NestPostSerializer(serializers.ModelSerializer):
    user_id = CreateUserSerializer()
    class Meta:
        model = PostModel
        fields = ['post_id', 'user_id', 'post_name', 'image', 'description', 'date', 'reason', 'status']  


# TO POSTING DATA TO DATABASE::::
class PostUserSerializer(serializers.ModelSerializer):
    class Meta:    
        model = User
        fields = ['id', 'username', 'email', 'password']

class PostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['post_id', 'user_id', 'post_name', 'image', 'description', 'date', 'reason', 'status']  

class ApprovePostSerializer(serializers.ModelSerializer):
    user_id = PostUserSerializer()
    class Meta:
        model = PostModel
        fields = ['post_id', 'user_id', 'post_name', 'image', 'description', 'date', 'reason', 'status']  


class NestUserPostSerializer(serializers.ModelSerializer):
    username = PostPostSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

# class AdminTableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostModel
#         fields = ['post_id', 'user_id', 'post_name', 'image', 'description', 'date', 'reason', 'status']

    # def get_status(self, obj):
    #     data = PostModel.objects.filter(status__isnull=True).all()
    #     return data 

# POST DATA ISIDE THE USER DATA::::
class WholeDataSerializer(serializers.ModelSerializer):
    post_details = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'post_details']

    def get_post_details(self, obj):
        data = PostModel.objects.filter(user_id=obj.id).values()
        return data    