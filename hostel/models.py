from django.db import models
class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)  # Set as primary key
    capacity = models.IntegerField()  # Capacity of the room
    occupied = models.BooleanField(default=False)  # Boolean field to check if the room is occupied

    def __str__(self):
        return f"Room {self.room_number}"
