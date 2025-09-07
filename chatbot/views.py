import json
import os
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def chatbot_home(request):
    return render(request, 'chatbot/chatbot.html')


@csrf_exempt
@require_POST
def ask_bot(request):
    data = json.loads(request.body)
    user_message = data.get("message", "").strip()

    # Load hostel JSON data
    info_path = os.path.join(settings.BASE_DIR, 'chatbot', 'hostel_info.json')
    try:
        with open(info_path, 'r', encoding='utf-8') as f:
            hostel_info = json.load(f)
    except Exception as e:
        return JsonResponse({"reply": f"⚠️ Could not load hostel info: {str(e)}"})

    # Convert JSON to a readable string to pass as system context
    hostel_context = json.dumps(hostel_info, indent=2)

    # Mistral AI request
    mistral_api_key = "w6Hukn9XI9JXxpQ0ML66jd4Qx7fC6oe9"
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {mistral_api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    system_message = (
        f"You are a helpful assistant for a hostel. Use ONLY the following data to answer user questions. "
        f"If the answer is not available, politely say you don't know.\n\nHostel Data:\n{hostel_context}"
    )

    payload = {
        "model": "open-mixtral-8x22b",
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 400
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            reply = result["choices"][0]["message"]["content"]
        else:
            reply = "❌ Sorry, I couldn't get a valid response from the AI."

        return JsonResponse({"reply": reply})

    except requests.exceptions.RequestException as e:
        return JsonResponse({"reply": f"⚠️ Error: {str(e)}"})
