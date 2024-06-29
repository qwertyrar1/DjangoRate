from django.shortcuts import render
from django.http import JsonResponse
from .get_rate_script import get_usd_to_rub_rate
from django.conf import settings


def exchange_rate(request):
    api_key = settings.ENV('API_KEY')
    return JsonResponse(get_usd_to_rub_rate(api_key), safe=False)
