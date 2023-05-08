from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from friend_api.serializers import UserSerializer
from friend_api.models import User


class InviteApiView(APIView):
    def patch(self, request, pk_user1, pk_user2):
        try:
            user1 = User.objects.get(pk=pk_user1)
            user2 = User.objects.get(pk=pk_user2)
        except:
            return Response({'error': f'Пользователя(ей) не существует'})
        try:
            if user1.friendList[f'{pk_user2}']['status'] == 'in friend':
                return Response({'error': f'Пользователи {user2.username} и {user1.username} уже друзья'})
            if user2.friendList[f'{pk_user1}']['status'] == 'outcoming':
                user1.add_in_friend(user1, user2)
                return Response(UserSerializer(user1).data['friendList'])
            else:
                user1.invite(user1, user2)
                return Response(user1.friendList)
        except:
            user1.invite(user1, user2)
            return Response(user1.friendList)

    def delete(self, request, pk_user1, pk_user2):
        try:
            user1 = User.objects.get(pk=pk_user1)
            user2 = User.objects.get(pk=pk_user2)
        except:
            return Response({'error': f'Пользователя(ей) не существует'})
        deleted = UserSerializer(user1).data['friendList'][f'{pk_user2}']
        if user1.friendList[f'{pk_user2}']['status'] == 'in friend':
            user1.remove_from_friend(user1, user2)
            return Response(deleted)
        else:
            return Response({'error': f'Пользователь {user2.username} отсутствует в списке друзей'})


class RegistrationApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AcceptRejectApiView(APIView):
    # Пользователь 1 принимает заявку пользователя 2
    def delete(self, request, pk_user1, pk_user2):
        try:
            user1 = User.objects.get(pk=pk_user1)
            user2 = User.objects.get(pk=pk_user2)
        except:
            return Response({'error': f'Пользователя(ей) не существует'})
        try:
            if user2.friendList[f'{pk_user1}']['status'] == 'in friend':
                return Response({'error': f'Пользователи {user2.username} и {user1.username} уже друзья'})
            if user1.friendList[f'{pk_user2}']['status'] == 'incoming':
                user1.add_in_friend(user1, user2)
                return Response(UserSerializer(user1).data)
            else:
                return Response({'error': 'Отсутствует входящая заявка в друзья'})
        except:
            return Response({'error': 'Отсутствует входящая заявка в друзья'})

    # Пользователь 1 отклоняет заявку пользователя 2
    def patch(self, request, pk_user1, pk_user2):
        user1 = User.objects.get(pk=pk_user1)
        user2 = User.objects.get(pk=pk_user2)
        deleted = UserSerializer(user1).data['friendList'][f'{pk_user2}']['username']
        if user2.friendList[f'{pk_user1}']['status'] == 'in friend':
            return Response({'error': f'Пользователи {user2.username} и {user1.username} уже друзья'})
        if user1.friendList[f'{pk_user2}']['status'] == 'incoming':
            user1.friendList.pop(f'{pk_user2}')
            user2.friendList.pop(f'{pk_user1}')
            user1.save()
            user2.save()
            return Response({'reject': f'Заявка {user2.username} отклонена'})
        else:
            return Response({'error': 'Отсутствует входящая заявка в друзья'})


class FriendListApiView(APIView):
    def get(self, request, pk_user):
        return Response(UserSerializer(User.objects.get(pk=pk_user)).data['friendList'])


class FriendStatusApiView(APIView):
    def get(self, request, pk_user1, pk_user2):
        return Response(UserSerializer(User.objects.get(pk=pk_user1)).data['friendList'][f'{pk_user2}']['status'])
