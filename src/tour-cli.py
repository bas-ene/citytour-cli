from osm_lib import searchCity
import owm_lib
import ors_lib
import json, time

if __name__ == '__main__':

    config = json.load(open('./config.json'))

    #continue getting input until user enters 'done'
    city_names = []
    city = ''
    while city != 'done' and len(city_names) < 5:
        city = input('Enter city: ')
        if city != 'done':
            city_names.append(city)

    coords = []
    #get the lat and lon for each city
    for city in city_names:
        result = searchCity(city, 3)
        #for each possibile result, make the user decide
        print('Possible matches:')
        for j in range(len(result)):
            print(f'{j+1}. {result[j]["display_name"]}')
        i = int(input('insert the number of the correct match: '))
        if result != {}:
            coords.append([result[i-1]['lon'],  result[i-1]['lat']])
        time.sleep(1)
    
    # get the distance and travel time between each city
    json_response = ors_lib.getDistance(coords, config['ors_key'])
    lengths = ors_lib.getLengthsOfSegments(json_response)

    # get the weather for each city
    weather = []
    for city_coords in coords:
        weather.append(owm_lib.getWeather(city_coords, config['owm_key']))
    print(weather)
