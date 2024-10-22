from django import forms
from .models import Room,RoomAllocation
from .models import RoomAllocation,Room

class Allocation(forms.ModelForm):
    class Meta:
        model = RoomAllocation
        fields = ('user',)