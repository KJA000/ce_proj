from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Document
import textract

@csrf_exempt
def upload_document(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')
        combined_text = ""

        for uploaded_file in uploaded_files:
            document = Document(file=uploaded_file)
            document.save()
            text = textract.process(document.file.path).decode('utf-8')
            combined_text += text + " "

        return JsonResponse({'message': 'Files uploaded and combined successfully', 'combined_text': combined_text})
    return render(request, 'upload.html')

def get_converted_text(request, document_id):
    try:
        document = Document.objects.get(pk=document_id)
        if not document.converted:
            text = textract.process(document.file.path).decode('utf-8')
            document.converted_text = text
            document.converted = True
            document.save()

        return JsonResponse({'converted_text': document.converted_text})
    except Document.DoesNotExist:
        return JsonResponse({'message': 'Document not found'}, status=404)
