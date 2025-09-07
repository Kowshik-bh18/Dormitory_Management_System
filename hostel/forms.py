from django import forms
from .models import Room, RoomAllocation

# Reusable CSS classes
INPUT_CLASSES = 'form-control form-control-sm'


# ===================== Room Allocation Form =====================
class RoomAllocationForm(forms.ModelForm):
    class Meta:
        model = RoomAllocation
        fields = ('user',)
        widgets = {
            'user': forms.Select(attrs={'class': INPUT_CLASSES}),
        }


# ===================== Add Room Form =====================
class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_number': forms.Select(attrs={'class': INPUT_CLASSES}),
            'capacity': forms.Select(attrs={'class': INPUT_CLASSES}),
            # Add more fields if Room model has them
        }


# ===================== User Password Reset Form =====================
class UserPasswordResetForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=200,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your registered email"
        })
    )


# ===================== Admin Password Reset Form =====================
class AdminPasswordResetForm(forms.Form):
    email = forms.EmailField(
        label="Admin Email",
        max_length=200,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter admin email"
        })
    )

    secret_id = forms.CharField(
        label="Secret Admin ID",
        max_length=100,
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter secret admin ID"
        })
    )
