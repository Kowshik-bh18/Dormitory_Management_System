from django import forms
from .models import FoodTimetable

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = FoodTimetable
        exclude = ['id']  # Example: Exclude the 'id' field if you don't want to edit it
