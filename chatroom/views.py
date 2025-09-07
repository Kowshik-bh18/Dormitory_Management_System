from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Chats, Report
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def view_chatroom(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        message = request.POST.get('message')
        if message:
            chat = Chats.objects.create(user=request.user, message=message, created=timezone.now())
            return JsonResponse({
                'user': chat.user.username,
                'message': chat.message,
                'created': chat.created.strftime('%Y-%m-%d %H:%M:%S'),
                'profile': chat.user.profile.image.url if hasattr(chat.user, 'profile') and chat.user.profile.image else '/static/default-avatar.png'
            })
        return JsonResponse({'error': 'Empty message'}, status=400)

    # GET request
    chats = Chats.objects.all().order_by('created')
    context = {'chats': chats}
    return render(request, 'chatroom/index.html', context)


@login_required
def add_new_report(request):
    reports = Report.objects.filter(user=request.user)
    if request.method == 'POST':
        report_text = request.POST.get('report')
        if report_text:
            Report.objects.create(user=request.user, report=report_text)
    if request.user.is_superuser:
        reports = Report.objects.all()
    return render(request, 'chatroom/report.html', {'reports': reports})


@login_required
def recived_report(request, pk):
    report = Report.objects.get(pk=pk)
    report.recived = True
    report.save()
    return redirect('chatroom:report')
