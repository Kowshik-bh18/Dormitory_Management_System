from django.shortcuts import render,redirect,get_object_or_404
from .models import FoodTimetable
from .forms import TimeTableForm
# Create your views here.

def viewTimetable(request):
    timetable = FoodTimetable.objects.all()
    context = {'timetable':timetable}
    return render(request,'timetable/timetable.html',context)

def update_timetable_view(request, pk):
    timetable = get_object_or_404(FoodTimetable, pk = pk)

    if request.method == 'POST':
        form = TimeTableForm(request.POST, instance=timetable)
        if form.is_valid():
            form.save()
            return redirect('timetable:Foodtimetable')  # Replace with your redirect URL
    else:
        form = TimeTableForm(instance=timetable)

    return render(request, 'timetable/update_timetable.html', {'form': form, 'timetable': timetable})





    