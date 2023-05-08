from rest_framework import status
from rest_framework.reverse import reverse_lazy, reverse
from rest_framework.test import APITestCase
from friend_api.models import User
from friend_api.serializers import FriendModel, FriendSerializer


# noinspection DuplicatedCode
class FriendApiTests(APITestCase):
    @classmethod
    def add_test_user(cls):
        friend2 = FriendSerializer(FriendModel('Chel', 'incoming'))
        friend1 = FriendSerializer(FriendModel('Olyx', 'outcoming'))
        friend5 = FriendSerializer(FriendModel('Tashkent', 'in friend'))
        friend6 = FriendSerializer(FriendModel('Vasya', 'in friend'))
        user1 = User(pk=1, username='Olyx', friendList={2: friend2.data})
        user2 = User(pk=2, username='Chel', friendList={1: friend1.data})
        user3 = User(pk=3, username='Pavel')
        user4 = User(pk=4, username='Igor')
        user5 = User(pk=5, username='Tashkent', friendList={6: friend6.data})
        user6 = User(pk=6, username='Vasya', friendList={5: friend5.data})
        user1.save()
        user2.save()
        user3.save()
        user4.save()
        user5.save()
        user6.save()

    def test_register_user(self):
        url = 'https://127.0.0.1:8000%s' % reverse_lazy('register')
        data = {'username': 'Olyx'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'Olyx')

    def test_auto_invite_friend(self):
        url = 'https://127.0.0.1:8000%s' % reverse('invite_or_delete', args=[1, 2])
        self.add_test_user()
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=1).friendList['2']['status'], 'in friend')
        self.assertEqual(User.objects.get(pk=2).friendList['1']['status'], 'in friend')

    def test_invite_friend(self):
        url = 'https://127.0.0.1:8000%s' % reverse('invite_or_delete', args=[3, 4])
        self.add_test_user()
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=3).friendList['4']['status'], 'outcoming')
        self.assertEqual(User.objects.get(pk=4).friendList['3']['status'], 'incoming')

    def test_delete_friend(self):
        url = 'https://127.0.0.1:8000%s' % reverse('invite_or_delete', args=[5, 6])
        self.add_test_user()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=5).friendList, {})
        self.assertEqual(User.objects.get(pk=6).friendList, {})

    def test_accept_friend(self):
        url = 'https://127.0.0.1:8000%s' % reverse('accept_or_reject', args=[1, 2])
        self.add_test_user()
        response = self.client.put(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=1).friendList['2']['status'], 'in friend')
        self.assertEqual(User.objects.get(pk=2).friendList['1']['status'], 'in friend')

    def test_reject_friend(self):
        url = 'https://127.0.0.1:8000%s' % reverse('accept_or_reject', args=[1, 2])
        self.add_test_user()
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'reject': 'Заявка Chel отклонена'})

    def test_friend_list(self):
        url = 'https://127.0.0.1:8000%s' % reverse('friend_list', args=[5])
        self.add_test_user()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_status_friend(self):
        url = 'https://127.0.0.1:8000%s' % reverse('friend_status', args=[5, 6])
        self.add_test_user()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=6).friendList['5']['status'], 'in friend')


