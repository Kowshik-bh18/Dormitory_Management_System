from django.shortcuts import render, get_object_or_404,redirect
from .models import Room, RoomAllocation
from .forms import Allocation

def index(request):
    rooms = Room.objects.all()
    roomcount = rooms.count()
    context = {'rooms': rooms,'roomcount':roomcount}
    return render(request, 'hostel/index.html', context)

def allocation_view(request, pk):
    allocations = RoomAllocation.objects.filter(room = pk)
    room = Room.objects.get(room_number = pk)
    allocationscount = allocations.count()
    if(allocationscount == 8):
        room.occupied = True
        room.save()
    else:
        room.occupied = False
        room.save()
        print(room.occupied)
    print(allocationscount)
    print(room.room_number)
    context = {'allocations':allocations,'room':room,'allocationscount':allocationscount}
    return render(request,'hostel/allocation.html',context)


def delete(request, pk):
    allocated = get_object_or_404(RoomAllocation, pk=pk)
    allocated.delete()
    # Redirect to the 'index' page or wherever the allocations are listed
    return redirect('hostel:index')  # Or 'hostel:allocations' if that's correct


def update(request, pk):
    slot = get_object_or_404(RoomAllocation, pk = pk)
    form = Allocation(instance=slot)
    if(request.method == 'POST'):
        form = Allocation(request.POST,instance=slot)
        form.save()
        return redirect('hostel:index')
    return render(request,'hostel/update.html',{'form':form})

