from django.db import models
from accounts.models import UserProfile

class Notification(models.Model):
    id_notification = models.AutoField(primary_key=True)
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
