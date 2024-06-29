from django.http import JsonResponse
from django.utils import timezone
from .models import RateRequest
from .get_rate_script import get_usd_to_rub_rate
from django.conf import settings
import json


def exchange_rate(request):
    last_request = RateRequest.objects.order_by('-timestamp').first()

    now = timezone.now()
    current_rate = json.loads(get_usd_to_rub_rate(settings.ENV('API_KEY')))

    # Проверка, прошло ли 10 секунд с последнего запроса
    if last_request and (now - last_request.timestamp).total_seconds() < 10:
        pass
    else:
        current_rate_value = current_rate['USD_to_RUB']
        RateRequest.objects.create(rate=current_rate_value)

    last_10_requests = RateRequest.objects.all().order_by('-timestamp')[:10]

    response_data = [current_rate]
    last_requests = [
        {'timestamp': request.timestamp, 'rate': request.rate}
        for request in last_10_requests
    ]
    response_data.extend(last_requests)

    return JsonResponse(response_data, safe=False)
