from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .forms import RegForm, LoginForm, updateForm
from .models import Student, Announcements
from hostel.models import Room, RoomAllocation
from userprofile.models import Profile
from email.mime.image import MIMEImage
import os

# -------------------- Registration --------------------
@login_required
def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            # Create User
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Create Profile
            Profile.objects.create(user=user)

            # Create Student linked to User
            student = form.save(commit=False)
            student.user = user
            student.save()

            # ---------------- Email Sending ----------------
            subject = "Welcome to BCM Hostel Siddapura"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]

            context = {
                "student": student,
                "support_email": "bcmsupport@gmail.com"
            }

            html_content = render_to_string("admission/registration_email.html", context)

            email = EmailMultiAlternatives(subject, "", from_email, recipient_list)
            email.attach_alternative(html_content, "text/html")

            # Attach logo inline
            logo_path = os.path.join(settings.BASE_DIR, "static", "hostel.jpg")
            if os.path.exists(logo_path):
                with open(logo_path, "rb") as f:
                    logo = MIMEImage(f.read())
                    logo.add_header("Content-ID", "<hostel_logo>")
                    logo.add_header("Content-Disposition", "inline", filename="hostel.jpg")
                    email.attach(logo)

            email.send(fail_silently=True)
            # ------------------------------------------------

            return redirect('admission:index')
    else:
        form = RegForm()

    return render(request, 'admission/register.html', {'form': form})

# -------------------- Login --------------------
def LoginView(request):
    if request.user.is_authenticated:
        return redirect('admission:index')

    page = 'login'
    error = None
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('admission:index')
        else:
            error = "Invalid username or password"

    return render(request, 'admission/login.html', {'page': page, 'form': form, 'error': error})

# -------------------- Logout --------------------
def LogoutView(request):
    logout(request)
    return redirect('admission:login')

# -------------------- Dashboard --------------------
@login_required
def index(request):
    studentcount = Student.objects.count()
    allocated_user_ids = RoomAllocation.objects.values_list('user', flat=True).distinct()
    active_students = Student.objects.filter(user__in=allocated_user_ids).count()
    pending_students = studentcount - active_students
    roomcount = Room.objects.count()

    occupied_rooms = 0
    for room in Room.objects.all():
        allocations = RoomAllocation.objects.filter(room=room).count()
        if allocations >= room.capacity:
            occupied_rooms += 1

    available_rooms = roomcount - occupied_rooms
    occupancy_percentage = round((occupied_rooms / roomcount) * 100, 1) if roomcount else 0

    announcements = Announcements.objects.all().order_by('-created')[:3]

    # Room allocation for logged-in user (normal users)
    if not request.user.is_superuser:
        allocation = RoomAllocation.objects.filter(user=request.user).first()
        if allocation:
            room_details = {
                'room_number': allocation.room.room_number,
            }
        else:
            room_details = None
    else:
        room_details = None  # superuser doesn't see single user room info

    context = {
        'studentcount': studentcount,
        'active_students': active_students,
        'pending_students': pending_students,
        'roomcount': roomcount,
        'occupied_rooms': occupied_rooms,
        'available_rooms': available_rooms,
        'occupancy_percentage': occupancy_percentage,
        'announcements': announcements,
        'room_details': room_details,
    }

    return render(request, 'admission/index.html', context)

# -------------------- View Students --------------------
@login_required
def viewStudents(request):
    students = Student.objects.select_related('user', 'room').all()
    room_allocations = {}
    allocations = RoomAllocation.objects.select_related('room', 'user').all()

    for allocation in allocations:
        if allocation.user:
            room_allocations[allocation.user.id] = allocation.room

    students_with_allocations = []
    for student in students:
        student_data = {
            'student': student,
            'allocated_room': room_allocations.get(student.user.id if student.user else None)
        }
        students_with_allocations.append(student_data)

    total_students = students.count()
    students_with_room_allocation = len([s for s in students_with_allocations if s['allocated_room']])
    students_without_room_allocation = total_students - students_with_room_allocation

    context = {
        'students': students,
        'students_with_allocations': students_with_allocations,
        'total_students': total_students,
        'students_with_room_allocation': students_with_room_allocation,
        'students_without_room_allocation': students_without_room_allocation,
    }

    return render(request, 'admission/students.html', context)

# -------------------- Delete Student --------------------
@login_required
def deletestudent(request, pk):
    student_user = get_object_or_404(User, pk=pk)
    RoomAllocation.objects.filter(user=student_user).delete()
    student_user.delete()
    return redirect('admission:viewstudents')

# -------------------- Update Student Details --------------------
@login_required
def updatedetails(request, pk):
    user = get_object_or_404(User, pk=pk)
    student = get_object_or_404(Student, user=user)
    form = updateForm(instance=student)

    if request.method == 'POST':
        form = updateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('admission:viewstudents')

    current_allocation = RoomAllocation.objects.filter(user=user).first()

    context = {
        'form': form,
        'student': student,
        'current_allocation': current_allocation
    }

    return render(request, 'admission/updateddetails.html', context)

# -------------------- Announcements --------------------
@login_required
def announcement_view(request):
    if request.method == 'POST':
        about = request.POST.get('about', '').strip()
        body = request.POST.get('body', '').strip()

        if about and body:
            Announcements.objects.create(
                about=about,
                body=body
            )
            return redirect("admission:announcement")

    announcements = Announcements.objects.all()
    total_announcements = announcements.count()

    context = {
        'announcements': announcements,
        'total_announcements': total_announcements,
    }

    return render(request, 'admission/announcement.html', context)

@login_required
def deleteAnnouncements(request, pk):
    announcement = get_object_or_404(Announcements, pk=pk)
    announcement.delete()
    return redirect("admission:announcement")
