import requests

def searchCity (cityName: str, limit: int) -> dict:
    END_POINT = "https://nominatim.openstreetmap.org/search"
    
    params = {
        "q": cityName,
        "format": "json",
        "addressdetails": 1,
        "limit": limit
    }
    
    response = requests.get(END_POINT, params=params)
    
    if response.status_code == 200:
        return response.json()
    return {}
