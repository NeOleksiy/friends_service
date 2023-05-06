from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from friend_api.serializers import UserSerializer, FriendModel, FriendSerializer
from friend_api.models import User


class UserApiView(APIView):
    def patch(self, request, pk_user1, pk_user2):
        user1 = User.objects.get(pk=pk_user1)
        user2 = User.objects.get(pk=pk_user2)
        incoming = FriendSerializer(FriendModel(user1.username, 'incoming'))
        outcoming = FriendSerializer(FriendModel(user2.username, 'outcoming'))
        user1.friendList[user2.pk] = outcoming.data
        user2.friendList[user1.pk] = incoming.data
        user1.save()
        user2.save()
        return Response(outcoming.data)









