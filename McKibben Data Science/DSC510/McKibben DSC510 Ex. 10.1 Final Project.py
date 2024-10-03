# DSC510
# Week 10
# Exercise 10.1
# Author: Makayla McKibben
# Date 08.05.2024

import requests
import json

# OOP Class and Methods
class getWeather:
    def __init__(self):
        print("Thank you for using this program to get the weather.")

    def zip_coor(self, zipcode):
        zip_url = 'http://api.openweathermap.org/geo/1.0/zip'
        zip_params = {'zip': zipcode, 'country': 'us', 'appid': '46144b694f4c99bebf7ec067bf779439'}
        try:
            zip_loc = requests.get(zip_url, params=zip_params)
            zip_lat = zip_loc.json()['lat']
            zip_lon = zip_loc.json()['lon']
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error, API address invalid.", end='\n')
            print(errh.args[0])
            print("Could not retrieve location information. Please try again.", end='\n')
        except requests.exceptions.ReadTimeout as errrt:
            print("Time out error, server took too long to respond.", end='\n')
            print("Could not retrieve location information. Please try again.", end='\n')
        except requests.exceptions.ConnectionError as conerr:
            print("Connection error, not able to connect to server.", end='\n')
            print("Could not retrieve location information. Please try again.", end='\n')
        except requests.exceptions.RequestException as errex:
            print("Exception request, non-specific error.", end='\n')
            print("Could not retrieve location information. Please try again.", end='\n')
        except:
            print("Could not find associated latitude and longitude. Please try again.")
        return zip_lat, zip_lon

    def city_state_coor(self, city, state):
        cit_url = 'http://api.openweathermap.org/geo/1.0/direct?'
        cit_param = {'q': city, 'state': state, 'country': 'us', 'limit': 5, 'appid': '46144b694f4c99bebf7ec067bf779439'}
        cit_loc = requests.get(cit_url, params=cit_param)
        print(cit_loc.json())
        state_abb = {
            'al': 'Alabama', 'ak': 'Alaska', 'ar': 'Arkansas', 'az': 'Arizona', 'ca': 'California',
            'co': 'Colorado', 'ct': 'Connecticut', 'de': 'Delaware', 'dc': 'District of Columbia',
            'fl': 'Florida', 'ga': 'Georgia', 'hi': 'Hawaii', 'id': 'Idaho', 'il': 'Illinois',
            'in': 'Indiana', 'ia': 'Iowa', 'ks': 'Kansas', 'ky': 'Kentucky', 'la': 'Louisiana',
            'me': 'Maine', 'md': 'Maryland', 'ma': 'Massachusetts', 'mi': 'Michigan', 'mn': 'Minnesota',
            'ms': 'Mississippi', 'mo': 'Missouri', 'mt': 'Montana', 'ne': 'Nebraska', 'nv': 'Nevada',
            'nh': 'New Hampshire', 'nj': 'New Jersey', 'nm': 'New Mexico', 'ny': 'New York',
            'nc': 'North Carolina', 'nd': 'North Dakota', 'oh': 'Ohio', 'ok': 'Oklahoma', 'or': 'Oregon',
            'pa': 'Pennsylvania', 'ri': 'Rhode Island', 'sc': 'South Carolina', 'sd': 'South Dakota',
            'tn': 'Tennessee', 'tx': 'Texas', 'ut': 'Utah', 'vt': 'Vermont', 'va': 'Virginia',
            'wa': 'Washington', 'wv': 'West Virginia', 'wi': 'Wisconsin', 'wy': 'Wyoming'}
        multi = []
        for i in range(0, 4, 1):
            multi.append(cit_loc.json()[i]['state'])
            print(multi)
        try:
            for i in range(0, len(multi)):
                print(multi[i])
                print(state_abb.get(state))
                if multi[i] == state_abb.get(state):
                    cit_url = 'http://api.openweathermap.org/geo/1.0/direct?'
                    cit_param = {'q': city, 'state': state, 'country': 'us', 'limit': 5,
                                 'appid': '46144b694f4c99bebf7ec067bf779439'}
                    cit_loc = requests.get(cit_url, params=cit_param)
                    cit_lat = cit_loc.json()[i]['lat']
                    cit_lon = cit_loc.json()[i]['lon']
                if i == len(multi) - 1 & multi[i] != state_abb.get(state):
                    print("Could not locate city state combination specified. Please try again.")
                    continue
        except TypeError:
            print("Invalid city state combination specified.")
        return cit_lat, cit_lon

    def city_state_info(self, lat, lon):
        cit_rev_url = 'http://api.openweathermap.org/geo/1.0/reverse'
        cit_rev_param = {'lat': lat, 'lon': lon, 'limit': 1, 'appid': '46144b694f4c99bebf7ec067bf779439'}
        cit_rev_info = requests.get(cit_rev_url, params=cit_rev_param)
        print(cit_rev_info.json()[0]['name'])
        print(cit_rev_info.json()[0]['state'])

    def forecast(self, lat, lon, units):
        forecast_url = 'https://api.openweathermap.org/data/2.5/forecast'
        fc_param = {'lat': lat, 'lon': lon, 'units': units, 'appid': '46144b694f4c99bebf7ec067bf779439'}
        fc_get = requests.get(forecast_url, params = fc_param)

        if units == 'imperial':
            speed = 'mph'
            temp = '°F'
        elif units == 'metric':
            speed = 'm/s'
            temp = '°C'
        elif units == 'standard':
            speed = 'm/s'
            temp = 'K'

        date = (fc_get.json()['list'][0]['dt_txt']).split(' ')[0]
        print("Weather for: ", date, end='\n')
        print("Current temp: ", fc_get.json()['list'][0]['main']['temp'], temp, end='\n')
        print("Feels like temp:", fc_get.json()['list'][0]['main']['feels_like'], temp, end='\n')
        print("Minimum temp today: ", fc_get.json()['list'][0]['main']['temp_min'], temp, end='\n')
        print("Maximum temp today: ", fc_get.json()['list'][0]['main']['temp_max'], temp, end='\n')
        print("Current pressure is: ", fc_get.json()['list'][0]['main']['pressure'], "hPa", end='\n')
        print("Current humidity is: ", fc_get.json()['list'][0]['main']['humidity'], "%", end='\n')
        print("Current wind speed is: ", fc_get.json()['list'][0]['wind']['speed'], speed, end='\n')
        print("Current weather description: ", fc_get.json()['list'][0]['weather'][0]['main'], "with",
              fc_get.json()['list'][0]['weather'][0]['description'], end='\n\n')

        for i in range(1, 40, 8):
            date_fc = (fc_get.json()['list'][i]['dt_txt']).split(' ')[0]
            print("Weather for: ", date_fc, end='\n')
            print("Forecasted minimum temp: ", fc_get.json()['list'][i]['main']['temp_min'], temp, end='\n')
            print("Forecasted maximum temp: ", fc_get.json()['list'][i]['main']['temp_max'], temp, end='\n')
            print("Forecasted pressure is: ", fc_get.json()['list'][i]['main']['pressure'], "hPa", end='\n')
            print("Forecasted humidity is: ", fc_get.json()['list'][i]['main']['humidity'], "%", end='\n')
            print("Forecasted wind speed is: ", fc_get.json()['list'][i]['wind']['speed'], speed,  end='\n')
            print("Forecasted weather description: ",
                  fc_get.json()['list'][i]['weather'][0]['main'], "with",
                  fc_get.json()['list'][i]['weather'][0]['description'], end='\n\n')


def main():
    print("This program will take a zipcode or city/state combination to lookup weather in the specified area.", end = '\n')
    print("You may indicate whether you would like to receive the temperature in Celsius, Fahrenheit, or Kelvin.", end = '\n')
    print("You may use this program as many times as you wish by entering the location information when prompted.", end = '\n')
    print("If you wish to exit at any time, enter quit to stop the program.", end = '\n')

    use_prog = ""
    while use_prog != 'quit':
        use_prog = input("Would you like to use the program? (Yes/Quit) ")
        use_prog = use_prog.lower()
        if use_prog == 'quit':
            exit()
        elif use_prog != 'yes' and use_prog != 'quit':
            print("Invalid entry. Please enter either 'yes' or 'quit'.", end = '\n')
            continue
        elif use_prog == 'yes':
            get_weather = getWeather()
            zip_or_city = ""
            while zip_or_city != 'quit':
                zip_or_city = input("Would you like to enter the zipcode or city/state combination for the location? (Zip/City): ")
                zip_or_city = zip_or_city.lower()
                if zip_or_city == 'quit':
                    exit()
                while zip != 'quit':
                    if zip_or_city == 'zip':
                        zip = input("Enter five digit zipcode: ")
                        if len(zip) != 5:
                            print("Not a valid zipcode, try again.")
                            continue
                        if len(zip) == 5:
                            try:
                                zip = int(zip)
                                pass
                            except ValueError:
                                print("Not a valid zipcode, try again.")
                                continue
                        try:
                            zip_lat, zip_lon = get_weather.zip_coor(zip)
                            print("The associated latitude and longitude is: ", "lat = ", zip_lat, "lon = ", zip_lon)
                            pass
                        except ValueError:
                            print("Unable to retrieve forecast, try again.")
                            continue
                        try:
                            units = "imperial"
                            while units != 'quit':
                                units = input("Would you like your values in imperial, metric, or scientific? (Imperial/Metric/Scientific): ")
                                units = units.lower()
                                if units == 'quit':
                                    exit()
                                if units == 'imperial':
                                    get_weather.forecast(zip_lat, zip_lon, units)
                                    get_weather.city_state_info(zip_lat, zip_lon)
                                    break
                                if units == 'metric':
                                    get_weather.forecast(zip_lat, zip_lon, units)
                                    get_weather.city_state_info(zip_lat, zip_lon)
                                    break
                                if units == 'scientific':
                                    units = "standard"
                                    get_weather.forecast(zip_lat, zip_lon, units)
                                    get_weather.city_state_info(zip_lat, zip_lon)
                                    break
                                else:
                                    print("Invalid units. Please enter imperial, metric, or scientific.")
                                    continue
                        except TypeError:
                            print("Not a valid zipcode, try again.")
                            continue
                if zip_or_city == 'city':
                    city = input("Enter city name: ")
                    city = city.lower()
                    while zip_or_city != 'quit':
                        state = input("Enter two letter state abbreviation: ")
                        try:
                            if len(state) != 2:
                                print("Not a valid state abbreviation, try again.")
                                continue
                            if len(state) == 2:
                                state = state.lower()
                                state_abb = {
                                'al' : 'Alabama', 'ak' : 'Alaska', 'ar' : 'Arkansas', 'az' : 'Arizona', 'ca' : 'California',
                                'co' : 'Colorado', 'ct' : 'Connecticut', 'de' : 'Delaware', 'dc' : 'District of Columbia',
                                'fl' : 'Florida', 'ga' : 'Georgia', 'hi' : 'Hawaii', 'id' : 'Idaho', 'il' : 'Illinois',
                                'in' : 'Indiana', 'ia' : 'Iowa', 'ks' : 'Kansas', 'ky' : 'Kentucky', 'la' : 'Louisiana',
                                'me' : 'Maine', 'md' : 'Maryland', 'ma' : 'Massachusetts', 'mi' : 'Michigan', 'mn': 'Minnesota',
                                'ms' : 'Mississippi', 'mo' : 'Missouri', 'mt' : 'Montana', 'ne' : 'Nebraska', 'nv' : 'Nevada',
                                'nh' : 'New Hampshire', 'nj' : 'New Jersey', 'nm' : 'New Mexico', 'ny' : 'New York',
                                'nc' : 'North Carolina', 'nd' : 'North Dakota', 'oh' : 'Ohio', 'ok' : 'Oklahoma', 'or' : 'Oregon',
                                'pa' : 'Pennsylvania', 'ri' : 'Rhode Island', 'sc' : 'South Carolina', 'sd' : 'South Dakota',
                                'tn' : 'Tennessee', 'tx' : 'Texas', 'ut' : 'Utah', 'vt' : 'Vermont', 'va' : 'Virginia',
                                'wa' : 'Washington', 'wv' : 'West Virginia', 'wi' : 'Wisconsin', 'wy' : 'Wyoming'}
                                try:
                                    # For loop to make sure the user put in a valid two letter abbreviation
                                    for i in range(0, len(state_abb.keys())):
                                        # Tells user they did not enter a valid abbreviation and loops again
                                        if state == (*state_abb,):
                                            pass
                                        if i == len(state_abb) and state != state_abb[i]:
                                            print("Please check your abbreviation and try again.", end='\n')
                                            continue
                                        # Increments the for loop if the user input was not a match to the
                                        # list indexed value
                                        elif i < len(state_abb):
                                            i += 1
                                except TypeError:
                                    print("Not a valid state, try again.")
                                try:
                                    cit_lat, cit_lon = get_weather.city_state_coor(city, state)
                                    print("The associated latitude and longitude is: ", "lat = ", cit_lat, "lon = ", cit_lon)
                                except TypeError:
                                    print("Not a valid city state combination, try again.")
                                    continue
                                try:
                                    units = "imperial"
                                    while units != 'quit':
                                        units = input("Would you like your values in imperial, metric, or scientific? (Imperial/Metric/Scientific): ")
                                        units = units.lower()
                                        if units == 'quit':
                                            exit()
                                        if units == 'imperial':
                                            get_weather.forecast(cit_lat, cit_lon, units)
                                            get_weather.city_state_info(cit_lat, cit_lon)
                                            break
                                        if units == 'metric':
                                            get_weather.forecast(zip_lat, zip_lon, units)
                                            get_weather.city_state_info(cit_lat, cit_lon)
                                            break
                                        if units == 'scientific':
                                            units = "standard"
                                            get_weather.forecast(cit_lat, cit_lon, units)
                                            get_weather.city_state_info(cit_lat, cit_lon)
                                            break
                                        else:
                                            print("Invalid units. Please enter imperial, metric, or scientific.")
                                            continue
                                    break
                                except TypeError:
                                    print("Invalid entry. Please try again.")
                                    continue
                        except ValueError:
                            print("You entered: ", city, ",", state, end = '\n')
                            print("Please check your spelling and try again.")
                            continue


    return
if __name__ == '__main__':
    main()