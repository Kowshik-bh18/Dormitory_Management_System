from django.db import models
from django.contrib.auth.models import User
from hostel.models import Room
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null = True,blank = True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null = True,blank = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100, null = False , blank = True)
    password1 = models.CharField(max_length = 100, null = False , blank = True)
    password2 = models.CharField(max_length = 100, null = False, blank = True)
    dob = models.DateField()
    gender = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone_number = models.IntegerField()
    address = models.TextField()
    admission_date = models.DateField(auto_now_add = True)
    # course (ForeignKey to a Course model, if needed)
    def __str__(self):
        return self.first_name
    