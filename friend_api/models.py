from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32)
    friendList = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.username

    @classmethod
    def add_in_friend(cls, user1, user2):
        user1.friendList[f'{user2.pk}']['status'] = 'in friend'
        user2.friendList[f'{user1.pk}']['status'] = 'in friend'
        user1.save()
        user2.save()

    @classmethod
    def remove_from_friend(cls, user1, user2):
        user1.friendList.pop(f'{user2.pk}')
        user2.friendList.pop(f'{user1.pk}')
        user1.save()
        user2.save()

    @classmethod
    def invite(cls, user1, user2):
        incoming = {'username': f'{user1.username}', 'status': 'incoming'}
        outcoming = {'username': f'{user2.username}', 'status': 'outcoming'}
        user1.friendList[user2.pk] = outcoming
        user2.friendList[user1.pk] = incoming
        user1.save()
        user2.save()
