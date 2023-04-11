import json as js
from .configs import get_config
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

config = get_config('.env')
def telegram(form):

    token = config.bot.token
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": '291870728',
        "text": f"{form}",
    }
    # Send the POST request to the Telegram bot API
    response = requests.post(url, data=payload)
    print(response.text)

    # Check the response status code
    if response.status_code == 200:
        return "Message sent successfully."
    else:
        print("Failed to send message.")
@csrf_exempt
def handler(request):
    data = js.loads(request.body)
    telegram(data)
    return HttpResponse(data['name'])
