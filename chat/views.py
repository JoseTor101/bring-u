from django.shortcuts import render, redirect, get_object_or_404
from .models import Chat, Message  # Import your models
from accounts.models import UserProfile  # Import your UserProfile model
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from .decorator import is_chat_member

@login_required
def Chats(request):
    user = request.user
    current_user = UserProfile.objects.get(username=user)

    chats = []
    if current_user: 
        chats = Chat.objects.filter(fk_id_delivery__fk_id_delivery_man=current_user)

    context = {
        'chats':chats
    }
    return render(request, 'chats.html', context)


@login_required
@is_chat_member
def Conversation(request, id_chat):
    user = request.user
    current_user = UserProfile.objects.get(username=user)
    chat = get_object_or_404(Chat, pk=id_chat)
    messages = Message.objects.filter(fk_id_chat=chat)

    context = {
        'user':user,
        'chat': chat,
        'messages': messages
        }

    if request.method == 'GET':
        #if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            # Check if it's an AJAX request
            messages_list = [
                {
                    'user': message.sender.username,
                    'value': message.content,
                    'date': message.timestamp.strftime("%b. %d, %Y, %I:%M %p")
                }
                for message in messages
            ]
           # return JsonResponse({'messages': messages_list})
        #else:
            # For regular page request, return the HTML page
            return render(request, 'conversation.html', context)
        
    """if request.method == 'POST':
        content = request.POST.get('content')

        # Create a new Message instance
        message = Message.objects.create(
            fk_id_chat=chat,
            sender=current_user,
            content=content,
            timestamp=timezone.now()
        )

        # Update the last_update field of the associated chat
        chat.last_update = timezone.now()
        chat.save()
       
        return JsonResponse({'success': True}) """

