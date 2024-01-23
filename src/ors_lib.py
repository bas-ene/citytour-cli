import requests

def getDistance(coordinates: list, auth_token: str) -> dict:
    API_ENDPOINT = 'https://api.openrouteservice.org/v2/directions/driving-car'
    
    body = {
        "coordinates": coordinates,
        "geometry": False,
    }

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml; charset=utf-8',
        'Authorization': auth_token,
        'Content-Type': 'application/json; charset=utf-8'
    }
    
    response = requests.post(url = API_ENDPOINT, json = body, headers = headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def getLengthsOfSegments (json_response: dict) -> list:
    lengths = []
    for segment in json_response['routes'][0]['segments']:
        lengths.append(segment['distance'])
    return lengths
