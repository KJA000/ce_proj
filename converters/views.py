from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Document
import docx2txt 
import tempfile
import os

@csrf_exempt
def upload_and_combine(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')
        combined_text = ""

        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_path = temp_file.name

            try:
                text = docx2txt.process(temp_file_path)
                combined_text += text + " "
            except Exception as e:
                print(f"Error extracting text from file {uploaded_file.name}: {str(e)}")

            os.remove(temp_file_path)

        doc_id = create_document_and_store_text(combined_text)
        
        return JsonResponse({'message': 'Files uploaded and combined successfully', 'doc_id':doc_id, 'combined_text': combined_text})

@csrf_exempt
def create_document_and_store_text(combined_text):
    document = Document()
    document.converted_text = combined_text
    document.converted = True
    document.save()

    return document.id
