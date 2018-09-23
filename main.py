import weather as w

# user actions


def getUserAction(availableOperations=None):
    while True:
        try:
            operation = int(input())
            if availableOperations is None:
                return operation
            if operation in availableOperations:
                return operation
            else:
                print('Type a number between 1-' + str(availableOperations[-1]))
        except ValueError:
            print('You must type a valid number!')


def loadingData(citiesId):
    print('Loading data...')

    data = w.getWeatherData(citiesId, w.c.CONST_CITY_WEATHER_BASE_URL)

    return data


def printData(data):
    w.printWeatherData(data)
    print('Completed successfully.\n\n')


def exportDataCSV(data):
    w.getCSVReport(data)
    print('Sucessfully exported.\n\n')


def outputDataToUser(data):

    print('Your data is ready! What do you want to do?\n(1) - Print\n(2) - Export CSV')

    reportOption = getUserAction([1, 2])

    # (1) print in terminal
    if reportOption == 1:
        printData(data)
    # (2) export to CSV
    else:
        exportDataCSV(data)


def runGetWeather():

    print('--------------getWeather()--------------\n')

    while True:
        print('Type a number:\n(1) - Select a city by ID\n(2) - Select all capitals\n(3) - Exit')

        action = getUserAction([1, 2, 3])

        # (1) specific city id
        if action == 1:

            print('Type city ID:')

            cityId = getUserAction()

            data = loadingData([str(cityId)])

            if data:
                outputDataToUser(data)
            else:
                print('No data available.\n\n')

        # (2) all capitals of Brazil
        elif action == 2:

            data = loadingData(w.c.CONST_BRAZILIAN_STATE_CAPITAL)

            if data:
                outputDataToUser(data)
            else:
                print('No data available.\n\n')

        # (3) Exit program
        else:
            print('Bye.')
            break


runGetWeather()
