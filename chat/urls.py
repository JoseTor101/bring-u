from django.urls import path
from . import views

urlpatterns = [
 path('', views.Chats, name='chats'),
 path('conversation/<int:id_chat>/', views.Conversation, name='conversation'),
]