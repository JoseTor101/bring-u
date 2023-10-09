from django.shortcuts import render, redirect, get_object_or_404
from .models import Chat, Message  # Import your models
from accounts.models import UserProfile  # Import your UserProfile model
from django.utils import timezone
from django.http import JsonResponse
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


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


def Conversation(request, id_chat):
    user = request.user
    current_user = UserProfile.objects.get(username=user)
    chat = get_object_or_404(Chat, pk=id_chat)
    messages = Message.objects.filter(fk_id_chat=chat)

    context = {
        'user': user,
        'chat': chat,
        'messages': messages,
        'chatId': chat.id_chat,
    }


    return render(request, 'conversation.html', context)