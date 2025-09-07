from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Profile
from .forms import UserForm, ProfileForm

@login_required
def index(request):
    """
    Display user profiles:
    - Superuser: sees all non-superuser users, searchable by username/email
    - Normal users: see only their own profile
    """
    query = request.GET.get('q', '').strip()  # remove extra spaces

    if request.user.is_superuser:
        users = User.objects.filter(is_superuser=False)  # exclude superusers
        if query:
            users = users.filter(
                Q(username__icontains=query) |
                Q(email__icontains=query)
            )
    else:
        users = User.objects.filter(id=request.user.id)  # normal user sees only themselves

    context = {
        'users': users,
        'query': query,
    }
    return render(request, 'userprofile/profile.html', context)


@login_required
def edit_profile(request, user_id):
    """
    Allow normal users to edit their own profile. Superuser cannot edit other users here.
    """
    user = get_object_or_404(User, id=user_id)

    # Prevent superuser from editing other profiles
    if request.user.is_superuser:
        return redirect('userprofile:index')

    # Only allow editing of own profile
    if request.user != user:
        return redirect('userprofile:index')

    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('userprofile:index')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'userprofile/edit_profile.html', context)
