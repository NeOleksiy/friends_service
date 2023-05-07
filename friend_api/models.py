from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32)
    friendList = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.username
