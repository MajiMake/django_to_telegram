import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json as js


def telegram(form):
    token = '1759600278:AAGWpC48yFaSz_YbFXOjDcqAPX6vkeIIPJk'
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": '-1001961235572',
        "text": f"{form}",
    }
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return HttpResponse("Message sent successfully.")
    else:
        return HttpResponse("Failed to send message.")


@csrf_exempt
def handler(request):
    text = ''
    data: dict = js.loads(request.body)['params']
    for key, value in data.items():  # reversed(data.items()):
        text += f'{key}\n{value}\n\n'
    return telegram(text)
