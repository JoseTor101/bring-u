from django.shortcuts import render
from .models import Notification

def notification_view(request):
    user = request.user
    notifications = Notification.objects.filter(recipient=user).order_by('-timestamp')
    unread_notifications = notifications.filter(is_read=False)
    notifications.update(is_read=True)
    
    return render(request, 'notifications.html', {'notifications': notifications, 'unread_notifications': unread_notifications})
