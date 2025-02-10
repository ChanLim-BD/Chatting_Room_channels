from django.db import models
from accounts.models import User 


class Room(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_room_set")

    class Meta:
        ordering = ["-pk"]

    @property
    def chat_group_name(self):
        return self.make_chat_group_name(room=self)
    
    @staticmethod
    def make_chat_group_name(room=None, room_pk=None):
        return "chat-%s" % (room_pk or room.pk)