from django.shortcuts import render
from .models import Room
# Create your views here.

def index(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'hostel/index.html',context)

