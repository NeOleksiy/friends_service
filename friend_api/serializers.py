from rest_framework import serializers
from friend_api.models import User


class FriendModel:
    def __init__(self, username, status):
        self.username = username
        self.status = status


class FriendSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32)
    status = serializers.CharField(max_length=20)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'friendList']
