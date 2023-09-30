from django.shortcuts import render, redirect, get_object_or_404
from .models import Chat, Message  # Import your models
from accounts.models import UserProfile  # Import your UserProfile model
from django.utils import timezone

def Chats(request):
    # Your code to fetch and display a list of chats
    return render(request, 'chats.html')

def Conversation(request, id_chat):
    chat = get_object_or_404(Chat, pk=id_chat)
    messages = Message.objects.filter(fk_id_chat=chat)
    return render(request, 'conversation.html', {'chat': chat, 'messages': messages})
