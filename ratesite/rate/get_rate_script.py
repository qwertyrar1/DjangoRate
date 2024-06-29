import requests
import json


def get_usd_to_rub_rate(api_key):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'RUB' in data['conversion_rates']:
            usd_to_rub_rate = data['conversion_rates']['RUB']
            return json.dumps({'USD_to_RUB': usd_to_rub_rate})
        else:
            return json.dumps({'error': 'RUB rate not found in response'})
    else:
        return json.dumps({'error': f'Failed to fetch data, status code: {response.status_code}'})
