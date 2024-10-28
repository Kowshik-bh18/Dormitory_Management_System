from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now  # Import timezone.now

class Chats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(default=now, blank=True)  # Use default=now

    def __str__(self):
        return self.message
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    recived = models.BooleanField(default=False)
    def __str__(self):
            return f"{self.user.username}"