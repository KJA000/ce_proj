from django.http import JsonResponse, HttpResponse
import requests
import time

def hugging_face_api_request(question, context):
    HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/wogkr810/mnm"
    HUGGING_FACE_API_KEY = "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"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}

    payload = {
        "inputs": {
                "question": "혁승이형 학교는 어디야?",
                "context": "이혁승은 경희대학교 인공지능학과 22학번이다."
        }
    }

    print("Payload:", payload)
    
    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
    return response.json()



def chatbot_view(request):
    question = request.POST.get('question')
    context = request.POST.get('context')

    api_response = hugging_face_api_request(question, context)

    return JsonResponse(api_response)

