import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json as js
import aiogram


async def telegram(form):

    token = 'token'
    bot: aiogram.Bot = aiogram.Bot(token)
    await bot.send_message('chat_id', form)


@csrf_exempt
async def handler(request):
    text = ''
    data: dict = js.loads(request.body)['params']
    for key, value in data.items():
        text += f'{key}\n{value}\n\n'
    return HttpResponse(await telegram(text))
