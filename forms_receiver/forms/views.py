import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json as js
import aiogram
import asyncio


async def telegram(form):

    token = 'token'
    bot: aiogram.Bot = aiogram.Bot(token)
    await bot.send_message('chat_id', form)


@csrf_exempt
def handler(request):
    print('hih')
    text = ''
    data: dict = js.loads(request.body)['params']
    for key, value in data.items():
        text += f'{key}\n{value}\n\n'
    asyncio.run(telegram(text))
    return HttpResponse('OK')
