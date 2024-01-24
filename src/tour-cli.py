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
        city = input('Inserisci città o "done" per terminare:')
        if city != 'done':
            city_names.append(city)

    coords = []
    #get the lat and lon for each city
    for city in city_names:
        result = searchCity(city, 3)
        #for each possibile result, make the user decide
        print('Possibili risultati:')
        for j in range(len(result)):
            print(f'{j+1}. {result[j]["display_name"]}')
        i = int(input('Inserisci il numero corrispondente alla città desiderata:'))
        if result != {}:
            coords.append([result[i-1]['lon'],  result[i-1]['lat']])
        time.sleep(0.5)
    
    # get the distance and travel time between each city
    json_response = ors_lib.getDistance(coords, config['ors_key'])
    lengths = ors_lib.getLengthsOfSegments(json_response)

    # get the weather for each city
    weather = []
    for city_coords in coords:
        weather.append(owm_lib.getWeather(city_coords, config['owm_key']))
    

    print('----------------')
    for i in range(len(city_names)):
        wd = owm_lib.getWeatherInDay(weather[i], i)
        print(f'{city_names[i]}: {wd["main"]["temp"]}°C\t{wd["weather"][0]["description"]}')
        if(i < len(city_names)-1):
            print(f'Distanza fino alla prossima tappa: {lengths[i]/1000} km')
        print(f'{wd["dt_txt"]}')
        print('----------------')
