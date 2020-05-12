'''
OpenWeatherMap API, https://openweathermap.org/api
by city name --> api.openweathermap.org/data/2.5/weather?q={city name},{country code}

JSON parameters https://openweathermap.org/current#current_JSON
    weather.description Weather condition within the group
    main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
    wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
'''

import requests                                 # http requests library, e.g. requests.get(API_Call).json()

# Initialize variables, console loop
def main():
    # Console loop
    print('\nWelcome to the Web Services API Demonstrator\n')
#    input('Please press ENTER to continue!\n')

    testCases = {1: 'Current Weather, city = Houston',
               2: 'Current Weather, enter city name',
               3: 'Current Weather, invalid key',
               4: 'Current Weather, invalid city',
               5: 'Future: current weather, enter zip code',
               6: 'Future',
               7: 'Future',
               99: 'Exit this menu'}

    userInput(testCases)

    input('\n\nSay Bye-bye'.upper())

# Map user console input to a test case
# userChoices is a dictionary, key points to test case
# Includes user input exception handling
# Loop until user input is '99'
def userInput(userChoices):

    while True:
        print(' your choices'.upper(), '\t\t\tTest Case\n'.upper(), '-' * 55)

        for key, value in userChoices.items():
            print('\t', key, ' \t\t\t\t', value)
        try:
            choice = int(input("\nPlease enter the numeric choice for a Test Case \n\t --> ".upper()))
        except:
            print("\nSomething went wrong, please enter a numeric value!!!\n")
            continue

        if choice == 99:
            break

        menuExcept(choice)

# Map user menu selection (parameter) to module (function call)
def menuExcept(choice):

    city = "Houston"                                         #default city
    API_key = '5bd2695ec45f88d4c14d7b43fd06a230'             # Mulholland's key
    invalidAPI_key = 'fd38d62aa4fe1a03d86eee91fcd69f6e'      # used by You Tube video, not active 9/2018
    units = '&units=imperial'                                # API default is Kelvin and meters/sec
    invalidCity = city + '88' + 'abc'

    if choice == 1:
        JSON_Response = currentWeatherByCity(API_key, units, 'Houston')
        currentWeatherFields(JSON_Response)
    elif choice == 2:
        city = input('\tPlease enter a city name --> ')
        JSON_Response = currentWeatherByCity(API_key, units, city)
        currentWeatherFields(JSON_Response)
    elif choice == 3:
        JSON_Response = currentWeatherByCity(invalidAPI_key, units, 'chicago')
    elif choice == 4:
        JSON_Response = currentWeatherByCity(API_key, units, invalidCity)
    elif choice == 5:
        print('test case construction underway, come back soon!')
    elif choice == 6:
        print('test case construction underway, come back soon!')
    elif choice == 7:
        print('test case construction underway, come back soon!')

    else:
        print('Whatchu talking about Willis? Please try a valid choice!')

    input('*************** Press Enter to continue ******************\n\n'.upper())


# build the openweathermap REST Request
def currentWeatherByCity(key, units, city):
    city = '&q=' + city
    API_Call = 'http://api.openweathermap.org/data/2.5/weather?appid=' + key + city + units
    print('\tThe api http string -->    '  + API_Call)
    input('\t*** hit ENTER to execute the API GET request ***\n')

    jsonResponse = requests.get(API_Call).json()
    print(jsonResponse)
    return jsonResponse

# display selected values from the openweathermap REST response
def currentWeatherFields(response):
    input('\n\t*** hit ENTER to check out selected JSON values ***\n')
    print("\t Entire attribute of weather --> ", response['weather'])
    print('\tdescription -->  ', response['weather'][0]['main'])
    print('\twind speed, mph -->  ', response['wind']['speed'])
    print('\ttemperature, F -->  ', response['main']['temp'])

main()