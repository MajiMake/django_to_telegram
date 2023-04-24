import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json as js


def telegram(form):

    token = 'token'
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": 'chat_id',
        "text": f"{form}",
    }
    # Send the POST request to the Telegram bot API
    response = requests.post(url, data=payload)

    # Check the response status code
    if response.status_code == 200:
        return "Message sent successfully."
    else:
        return "Failed to send message."
@csrf_exempt
def handler(request):
    text = ''
    data: dict = js.loads(request.body)['params']
    for key, value in data.items():
        text += f'{key}\n{value}\n\n'
    return HttpResponse(telegram(text))
