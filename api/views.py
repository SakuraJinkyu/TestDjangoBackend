import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def weather_view(request):
    city = request.GET.get('city', 'Seoul')
    api_key = settings.WEATHER_API_KEY
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'Failed to fetch weather data'},
                            status=response.status_code)
