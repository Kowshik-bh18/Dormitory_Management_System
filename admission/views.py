from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegForm,LoginForm,updateForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Student, Announcements
from hostel.models import Room
from django import forms
from userprofile.models import Profile
@login_required
def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            # Create the user using the cleaned data from the form
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.set_password(form.cleaned_data['password1'])  # Hash the password
            user.save()  # Save the user to the database
            profile = Profile(user = user)
            profile.save()
            # Now save the registration info to the Student model
            student = form.save(commit=False)
            # Optionally link Student to User if there's a ForeignKey
            student.user = user  # Uncomment if you have a ForeignKey
            student.save()

            return redirect('admission:index') 
    else:
        form = RegForm()

    context = {'form': form}
    return render(request, 'admission/register.html', context)
def LoginView(request):
    page = 'login'
    error = False
    if(request.user.is_authenticated):
        return redirect('admission:index')
    form = LoginForm()  # Initialize the form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')  # Use cleaned_data
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('user logged in successfull')
                return redirect('admission:index')  # Ensure redirect is returned
            else:
                  error = "invalid user or password"
    context = {'page': page, 'form': form,'error':error}  # Include the form in context
    return render(request, 'admission/login.html', context)  # Pass context
@login_required
def index(request):
    studentcount = Student.objects.count()
    roomcount = Room.objects.count()
    announcements = Announcements.objects.all()[0:3]
    context = {'studentcount':studentcount,'roomcount':roomcount,'announcements':announcements}
    
    return render(request,'admission/index.html',context)

def LogoutView(request):
    logout(request)
    return redirect('admission:login')
@login_required
def veiewStudents(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request,'admission/students.html',context)
@login_required
def deletestudent(request, pk):
    student = User.objects.get(pk = pk)
    student.delete()
    return redirect('admission:viewstudents')
@login_required
def updatedetails(request, pk):
    user = User.objects.get(pk = pk)
    student = Student.objects.get(user = user)
    form = updateForm(instance=student)

    print(User.password)
    if request.method == 'POST':
        form = updateForm(request.POST, instance=student)
        print(user.username)
        if form.is_valid():
            commitform = form.save(commit = False)
            commitform.save()
            return redirect('admission:viewstudents')
        else:
            print(form.errors)  # Add this line to debug

    context = {'form':form}
    return render(request,'admission/updatedetails.html',context)



@login_required
def announcement_view(request):
    announcements = Announcements.objects.all()
    if(request.method == 'POST'):
        about = request.POST.get('about')
        body = request.POST.get('body')
        announcement = Announcements(
            about = about,body = body
        )
        announcement.save()
        return redirect("admission:announcement")
    context = {"announcements":announcements}
    return render(request,'admission/announcement.html',context)

@login_required
def deleteAnnouncements(request, pk):
    try:
        announcement = Announcements.objects.get(pk=pk)
        announcement.delete()
    except Announcements.DoesNotExist:
        pass  # You can handle the case when the announcement doesn't exist if needed

    return redirect("admission:announcement") 
    