# DSC510
# Week 10
# Exercise 10.1
# Author: Makayla McKibben
# Date 08.09.2024

import requests

# OOP Class and Methods
class getWeather:

    # This is just the initialization method for starting to use the object/methods
    def __init__(self):
        print("Thank you for using this program to get the weather.")

    # This method does the API call to get the coordinates from a zipcode and returns them to the main program
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
        except UnicodeEncodeError as err:
            print("Could not find associated latitude and longitude. Please try again.")
        return zip_lat, zip_lon

    # This was a little trickier to implement with all the potential for duplicate cities, spelling mistakes, and then making sure the state abbreviations were good.
    def city_state_coor(self, city, state):
        cit_url = 'http://api.openweathermap.org/geo/1.0/direct?'
        cit_param = {'q': city, 'state': state, 'country': 'us', 'limit': 5,
                'appid': '46144b694f4c99bebf7ec067bf779439'}
        try:
            cit_loc = requests.get(cit_url, params=cit_param)
        except IndexError:
            print("Could not find cities and states matching your request. Please try again.")
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


        # Create dictionary of states and they're abbreviations to show the user.
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

        # Create an empty list that will take the first five recommended locations based on what the user provided
        multi = []
        try:
            for i in range(0, 4, 1):
                multi.append(cit_loc.json()[i]['state'])
            select_state = state_abb.get(state)
            print(select_state)
            full_state_name = select_state
        except IndexError:
            print("Could not find city and state matching your request. Please try again.")

        # Check the list we made previously against the user input.
        for i in range(0, 4, 1):
            if multi[i] == select_state:
                cit_name = cit_loc.json()[i]['name']
                state_name = cit_loc.json()[i]['state']
                cit_lat = cit_loc.json()[i]['lat']
                cit_lon = cit_loc.json()[i]['lon']
                print("This weather is for: ", cit_name, ",", state_name)
                print("Latitude is: ", cit_lat, "and Longitude is: ", cit_lon)

                # Try blocks that take care of the get request
                try:
                    for i in range(0, 4):
                        if multi[i] == full_state_name:
                            try:
                                cit_url = 'http://api.openweathermap.org/geo/1.0/direct?'
                                cit_param = {'q': city, 'state': state, 'country': 'us', 'limit': 5,
                                             'appid': '46144b694f4c99bebf7ec067bf779439'}
                                cit_loc = requests.get(cit_url, params=cit_param)
                                cit_lat = cit_loc.json()[i]['lat']
                                cit_lon = cit_loc.json()[i]['lon']
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
                        elif i < 4:
                            i += 1
                        elif i == 4 & multi[i] != full_state_name:
                            print("Please try again.", end='\n')
                except TypeError:
                    print("Could not locate city state combination specified. Please try again.")
                    cit_state_no_exist = "Could not find associated city and state. Please try again."
                    print(cit_state_no_exist)
        return cit_lat, cit_lon

    # This method uses the latitude and longitude and gets the name and state
    def city_state_info(self, lat, lon):
        cit_rev_url = 'http://api.openweathermap.org/geo/1.0/reverse'
        cit_rev_param = {'lat': lat, 'lon': lon, 'limit': 1, 'appid': '46144b694f4c99bebf7ec067bf779439'}
        try:
            cit_rev_info = requests.get(cit_rev_url, params=cit_rev_param)
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
        print(cit_rev_info.json()[0]['name'])
        print(cit_rev_info.json()[0]['state'])

    # This method did most of the heavy lifting of calling for the actual weather information from the API
    def forecast(self, lat, lon, units):
        forecast_url = 'https://api.openweathermap.org/data/2.5/forecast'
        fc_param = {'lat': lat, 'lon': lon, 'units': units, 'appid': '46144b694f4c99bebf7ec067bf779439'}
        try:
            fc_get = requests.get(forecast_url, params=fc_param)
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

        # Takes the units input and labels the output data accordingly
        if units == 'imperial':
            speed = 'mph'
            temp = '°F'
        elif units == 'metric':
            speed = 'm/s'
            temp = '°C'
        elif units == 'standard':
            speed = 'm/s'
            temp = 'K'

        # This block of printed text is for the current weather data
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

        # This block of prints in a for loop will print the five day forecast
        for i in range(1, 40, 8):
            date_fc = (fc_get.json()['list'][i]['dt_txt']).split(' ')[0]
            print("Weather for: ", date_fc, end='\n')
            print("Forecasted minimum temp: ", fc_get.json()['list'][i]['main']['temp_min'], temp, end='\n')
            print("Forecasted maximum temp: ", fc_get.json()['list'][i]['main']['temp_max'], temp, end='\n')
            print("Forecasted pressure is: ", fc_get.json()['list'][i]['main']['pressure'], "hPa", end='\n')
            print("Forecasted humidity is: ", fc_get.json()['list'][i]['main']['humidity'], "%", end='\n')
            print("Forecasted wind speed is: ", fc_get.json()['list'][i]['wind']['speed'], speed, end='\n')
            print("Forecasted weather description: ",
                  fc_get.json()['list'][i]['weather'][0]['main'], "with",
                  fc_get.json()['list'][i]['weather'][0]['description'], end='\n\n')

# The main method is mostly used providing the user with info and keeping loops available for however many inputs the user wants to do
def main():
    print("This program will take a zipcode or city/state combination to lookup weather in the specified area.",
          end='\n')
    print("You may indicate whether you would like to receive the temperature in Celsius, Fahrenheit, or Kelvin.",
          end='\n')
    print("You may use this program as many times as you wish by entering the location information when prompted.",
          end='\n')
    print("If you wish to exit at any time, enter quit to stop the program.", end='\n')

    # Initial loop set up for making sure the user wants to use the program
    use_prog = ""
    while use_prog != 'quit':
        use_prog = input("Would you like to use the program? (Yes/Quit) ")
        use_prog = use_prog.lower()
        if use_prog == 'quit':
            exit()
        elif use_prog != 'yes' and use_prog != 'quit':
            print("Invalid entry. Please enter either 'yes' or 'quit'.", end='\n')
            continue
        elif use_prog == 'yes':
            #Initiates the object
            get_weather = getWeather()
            zip_or_city = ""
            # This is the loop that lets the user choose between city/state data entry or by zipcode
            while zip_or_city != 'quit':
                zip_or_city = input(
                    "Would you like to enter the zipcode or city/state combination for the location? (Zip/City/Quit): ")
                zip_or_city = zip_or_city.lower()
                if zip_or_city == 'quit':
                    exit()
                if zip_or_city == 'zip':
                    zip = ""
                    # If usser wants to enter the data using a zip code
                    while zip != 'quit':
                        if zip_or_city == 'zip':
                            zip = input("Enter five digit zipcode: ")
                            if zip == 'quit':
                                exit()
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
                                print("The associated latitude and longitude is: ", "lat = ", zip_lat, "lon = ",
                                      zip_lon)
                                pass
                            except ValueError:
                                print("Unable to retrieve forecast, try again.")
                                continue
                            except KeyError:
                                print("Unable to retrieve forecast due to invalid zipcode, try again.")
                                continue
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
                        try:
                            units = "imperial"
                            if units != 'quit':
                                units = input(
                                    "Would you like your values in imperial, metric, or scientific? (Imperial/Metric/Scientific/Quit): ")
                                units = units.lower()
                                if units == 'quit':
                                    exit()
                                if units == 'scientific':
                                    try:
                                        units = 'standard'
                                        get_weather.forecast(zip_lat, zip_lon, units)
                                        get_weather.city_state_info(zip_lat, zip_lon)
                                        break
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
                                if units == 'imperial':
                                    try:
                                        get_weather.forecast(zip_lat, zip_lon, units)
                                        get_weather.city_state_info(zip_lat, zip_lon)
                                        break
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
                                if units == 'metric':
                                    try:
                                        units = 'metric'
                                        get_weather.forecast(zip_lat, zip_lon, units)
                                        get_weather.city_state_info(zip_lat, zip_lon)
                                        break
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
                        except TypeError as errh:
                            print("TypeError encountered.", end='\n')
                        except ValueError as errh:
                            print("ValueError encountered.", end='\n')
                # If the user wants to use city/state
                if zip_or_city == 'city':
                    city = ""
                    while city != 'quit':
                        city = input("Enter city name: ")
                        try:
                            if city == 'quit':
                                exit()
                            city = city.lower()
                            break
                        except ValueError:
                            print("Not a valid city, try again.")
                            continue
                    state = ""
                    if state != 'quit':
                        print("The program will now print a list of abbreviations of states for you to choose from.",
                              end='\n')
                        state_abb = {
                            'al': 'Alabama', 'ak': 'Alaska', 'ar': 'Arkansas', 'az': 'Arizona',
                            'ca': 'California', 'co': 'Colorado', 'ct': 'Connecticut', 'de': 'Delaware',
                            'dc': 'District of Columbia', 'fl': 'Florida', 'ga': 'Georgia',
                            'hi': 'Hawaii', 'id': 'Idaho', 'il': 'Illinois', 'in': 'Indiana',
                            'ia': 'Iowa', 'ks': 'Kansas', 'ky': 'Kentucky', 'la': 'Louisiana',
                            'me': 'Maine', 'md': 'Maryland', 'ma': 'Massachusetts', 'mi': 'Michigan',
                            'mn': 'Minnesota', 'ms': 'Mississippi', 'mo': 'Missouri', 'mt': 'Montana',
                            'ne': 'Nebraska', 'nv': 'Nevada', 'nh': 'New Hampshire', 'nj': 'New Jersey',
                            'nm': 'New Mexico', 'ny': 'New York', 'nc': 'North Carolina',
                            'nd': 'North Dakota', 'oh': 'Ohio', 'ok': 'Oklahoma', 'or': 'Oregon',
                            'pa': 'Pennsylvania', 'ri': 'Rhode Island', 'sc': 'South Carolina',
                            'sd': 'South Dakota', 'tn': 'Tennessee', 'tx': 'Texas', 'ut': 'Utah',
                            'vt': 'Vermont', 'va': 'Virginia', 'wa': 'Washington', 'wv': 'West Virginia',
                            'wi': 'Wisconsin', 'wy': 'Wyoming'}
                        print(state_abb)
                        state = input("Enter two letter state abbreviation: ")
                        state = str(state.lower())
                        if state == 'quit':
                            exit()
                        if len(state) != 2:
                            print("Not a valid state abbreviation, try again.")
                            continue
                        if len(state) == 2:
                            if state in state_abb.keys():
                                pass
                            else:
                                print("Invalid state abbreviation, try again.")
                                continue
                        try:
                            cit_lat, cit_lon = get_weather.city_state_coor(city, state)
                            pass
                        except TypeError:
                            print("Not a valid city state combination, try again.")
                            continue
                        except IndexError:
                            print("Invalid city state pair, try again.")
                            continue
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
                        try:
                            units = "imperial"
                            while units != 'quit':
                                units = input(
                                    "Would you like your values in imperial, metric, or scientific? (Imperial/Metric/Scientific): ")
                                units = units.lower()
                                if units == 'quit':
                                    exit()
                                if units == 'imperial':
                                    try:
                                        get_weather.forecast(cit_lat, cit_lon, units)
                                        get_weather.city_state_info(cit_lat, cit_lon)
                                        break
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
                                if units == 'metric':
                                    try:
                                        get_weather.forecast(cit_lat, cit_lon, units)
                                        get_weather.city_state_info(cit_lat, cit_lon)
                                        break
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
                                if units == 'scientific':
                                    try:
                                        units = "standard"
                                        get_weather.forecast(cit_lat, cit_lon, units)
                                        get_weather.city_state_info(cit_lat, cit_lon)
                                        break
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
                                else:
                                    print("Invalid units. Please enter imperial, metric, scientific, or quit.")
                                    continue
                        except:
                            print("Not a valid city/state combination, try again.")
                            break
                continue
    return


if __name__ == '__main__':
    main()









