from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)  # Set as primary key
    capacity = models.IntegerField()  # Capacity of the room
    occupied = models.BooleanField(default=False)  # Boolean to check if occupied

    def __str__(self):
        return f"Room {self.room_number}"

class RoomAllocation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Renamed for clarity
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"Room {self.room.room_number} - {self.user.username}"
