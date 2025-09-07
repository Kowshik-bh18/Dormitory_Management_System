from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.forms import SetPasswordForm
from django.conf import settings

from .models import Room, RoomAllocation
from .forms import RoomAllocationForm, AddRoomForm, UserPasswordResetForm, AdminPasswordResetForm


# -------------------- List all rooms --------------------
@login_required
def index(request):
    rooms = Room.objects.all()
    for room in rooms:
        room.alloc_count = RoomAllocation.objects.filter(room=room, user__is_superuser=False).count()
    context = {'rooms': rooms, 'roomcount': rooms.count()}
    return render(request, 'hostel/index.html', context)


# -------------------- Add Room --------------------
@login_required
def addRoom(request):
    if request.method == "POST":
        room_number = request.POST.get('room_number')
        capacity = request.POST.get('capacity')
        if not room_number or not capacity:
            messages.error(request, "Room number and capacity are required.")
            return redirect('hostel:index')
        Room.objects.create(room_number=int(room_number), capacity=int(capacity))
        messages.success(request, f"Room {room_number} added successfully.")
        return redirect('hostel:index')
    return render(request, 'hostel/addroom.html')


# -------------------- Room Allocation View --------------------
@login_required
def allocation_view(request, pk):
    room = get_object_or_404(Room, pk=pk)
    allocations = RoomAllocation.objects.filter(room=room, user__is_superuser=False)
    alloc_count = allocations.count()
    room.occupied = alloc_count >= room.capacity
    room.save(update_fields=["occupied"])
    context = {
        'room': room,
        'allocations': allocations,
        'allocationscount': alloc_count,
    }
    return render(request, 'hostel/allocation.html', context)


# -------------------- Add Allocation --------------------
@login_required
def add(request):
    room_id = request.GET.get('q')
    if not room_id:
        messages.error(request, "No room specified for allocation.")
        return redirect("hostel:index")

    room = get_object_or_404(Room, pk=room_id)
    users = User.objects.exclude(
        id__in=RoomAllocation.objects.values_list('user_id', flat=True)
    ).exclude(is_superuser=True)

    if request.method == 'POST':
        user_id = request.POST.get('user')
        user = get_object_or_404(User, id=user_id)

        if RoomAllocation.objects.filter(room=room).count() >= room.capacity:
            messages.error(request, f"Room {room.room_number} is already full!")
            return redirect('hostel:allocations', pk=room.pk)

        if RoomAllocation.objects.filter(user=user).exists():
            messages.error(request, f"{user.username} is already allocated to another room!")
            return redirect('hostel:allocations', pk=room.pk)

        RoomAllocation.objects.create(user=user, room=room)
        room.occupied = RoomAllocation.objects.filter(room=room).count() >= room.capacity
        room.save(update_fields=["occupied"])

        messages.success(request, f"{user.username} allocated to Room {room.room_number}.")
        return redirect('hostel:allocations', pk=room.pk)

    context = {'users': users, 'room': room}
    return render(request, 'hostel/add.html', context)


# -------------------- Update Allocation --------------------
@login_required
def update(request, pk):
    allocation = get_object_or_404(RoomAllocation, pk=pk)
    form = RoomAllocationForm(instance=allocation)

    if request.method == 'POST':
        form = RoomAllocationForm(request.POST, instance=allocation)
        if form.is_valid():
            form.save()
            messages.success(request, "Allocation updated successfully.")
            return redirect('hostel:allocations', pk=allocation.room.pk)
        messages.error(request, "Error updating allocation.")

    return render(request, 'hostel/update.html', {'form': form})


# -------------------- Delete Allocation --------------------
@login_required
def delete(request, pk):
    allocation = get_object_or_404(RoomAllocation, pk=pk)
    room = allocation.room
    allocation.delete()
    room.occupied = RoomAllocation.objects.filter(room=room, user__is_superuser=False).count() >= room.capacity
    room.save(update_fields=["occupied"])
    messages.success(request, "Allocation deleted successfully.")
    return redirect('hostel:allocations', pk=room.pk)


# -------------------- Delete Room --------------------
@login_required
def deleteRoom(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room.delete()
    messages.success(request, "Room deleted successfully.")
    return redirect("hostel:index")


# -------------------- User Password Reset Request --------------------
def user_password_reset(request):
    if request.method == "POST":
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email, is_superuser=False)
            except User.DoesNotExist:
                messages.error(request, "No user found with this email.")
                return redirect("hostel:user_password_reset")

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # FIXED: Use the correct namespace pattern
            reset_url = request.build_absolute_uri(reverse("hostel:password_reset_confirm", args=[uid, token]))

            send_mail(
                "BCM Hostel Siddapura - Password Reset",
                f"Hello {user.username},\n\nPlease reset your password using the link below:\n{reset_url}\n\nBCM Hostel Siddapura",
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )

            messages.success(request, "Password reset link has been sent to your email.")
            return redirect('hostel:index')
    else:
        form = UserPasswordResetForm()
    return render(request, "hostel/user_password_reset.html", {"form": form})


# -------------------- Admin Password Reset Request --------------------
def admin_password_reset(request):
    if request.method == "POST":
        form = AdminPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            secret_id = form.cleaned_data["secret_id"]

            # Check secret admin ID
            if secret_id != settings.ADMIN_SECRET_ID:
                messages.error(request, "Invalid Secret Admin ID.")
                return redirect("hostel:index")  # redirect to login page

            # Check if admin exists
            try:
                user = User.objects.get(email=email, is_superuser=True)
            except User.DoesNotExist:
                messages.error(request, "No admin found with this email.")
                return redirect("hostel:index")  # redirect to login page

            # Generate password reset link
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(
                reverse("hostel:password_reset_confirm", args=[uid, token])
            )

            # Send email
            send_mail(
                "BCM Hostel Siddapura - Admin Password Reset",
                f"Hello Admin {user.username},\n\nThis reset was requested with Secret ID.\nUse the link below to reset your password:\n{reset_url}\n\nBCM Hostel Siddapura",
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )

            # Success message
            messages.success(request, "Admin password reset link has been sent to your email.")
            return redirect("hostel:index")  # redirect to login page
    else:
        form = AdminPasswordResetForm()

    # If GET request, show the reset form
    return render(request, "hostel/admin_password_reset.html", {"form": form})


# -------------------- Password Reset Confirm View --------------------
def user_password_reset_confirm(request, uidb64, token):
    from django.utils.http import urlsafe_base64_decode
    from django.contrib.auth.tokens import default_token_generator

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Password has been reset successfully.")
                return redirect('hostel:index')  # if your login view is inside hostel app
        else:
            form = SetPasswordForm(user)
        return render(request, "hostel/password_reset_confirm.html", {"form": form})
    else:
        messages.error(request, "The password reset link is invalid.")
        return redirect("hostel:user_password_reset")