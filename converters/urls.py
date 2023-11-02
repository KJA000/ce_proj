from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    path('convert/<int:document_id>/', views.get_converted_text, name='get_converted_text'),
]
