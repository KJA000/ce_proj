from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/<int:document_id>/', views.chatbot_view, name='chatbot'),
]