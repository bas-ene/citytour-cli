import requests

def getWeather(coords: list, owm_key: str) -> dict:
    API_ENDPOINT = 'api.openweathermap.org/data/2.5/forecast'
    
    response = requests.get(f'https://{API_ENDPOINT}?lat={coords[1]}&lon={coords[0]}&appid={owm_key}&units=metric&lang=it')
    
    if response.status_code == 200:
        return response.json()
    else:
        return {}
