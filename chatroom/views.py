from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Chats, Report
from django.contrib.auth.decorators import login_required

@login_required
def view_chatroom(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        message = request.POST.get('message')
        user = request.user

        # Save the chat message
        chat = Chats(user=user, message=message)
        chat.save()

        # Respond with the new chat data
        return JsonResponse({
            'user': user.username,
            'message': chat.message,
            'created': chat.created.strftime('%Y-%m-%d %H:%M:%S')
        })

    # For GET requests, render the template
    chats = Chats.objects.all()
    context = {'chats': chats}
    return render(request, 'chatroom/index.html', context)



@login_required
def add_new_report(request):
    reports = Report.objects.filter(user = request.user)
    if(request.method=='POST'):
        report = request.POST.get('report')
        newReport = Report(user = request.user,report = report)
        newReport.save()
    if(request.user.is_superuser):
        reports = Report.objects.all()
    context = {'reports':reports}
    return render(request,'chatroom/report.html',context)
@login_required
def recived_report(request, pk):
    report = Report.objects.get(pk = pk)
    report.recived = True
    report.save()
    return redirect('chatroom:report')