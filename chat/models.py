from django.db import models
from django.utils import timezone
from bring_u.models import Delivery
from accounts.models import UserProfile

class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    fk_id_delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

class Message(models.Model):
    id_message = models.AutoField(primary_key=True)
    fk_id_chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Update the last_update field of the associated chat
        self.fk_id_chat.last_update = timezone.now()
        self.fk_id_chat.save()
        super(Message, self).save(*args, **kwargs)