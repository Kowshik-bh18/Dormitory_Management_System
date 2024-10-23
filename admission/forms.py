from django import forms
from .models import Student, Room

class RegForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(2005,2025)))
    admission_date = forms.DateField(widget=forms.SelectDateWidget(years=(2024,2025)))
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('user',)
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class updateForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('password1','password2','user',)
