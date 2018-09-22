import weather as w

# user actions


def getUserAction(availableOperations):
    while True:
        try:
            operation = int(input())
            if operation in availableOperations:
                return operation
            else:
                print('Type a number between 1-' + str(availableOperations[-1]))
        except ValueError:
            print('You must type a valid number!')


while True:
    print('Type a number:\n(1) - Select a city by ID\n(2) - Select all capitals\n(3) - Exit')

    operation = getUserAction([1, 2, 3])

    # (1) specific city id
    if operation == 1:
        # todo
        print('Type a number:')
        # availableCitiesIds = []
        # availableCitiesIds.extend(range(1, w.c.CONST_BRAZILIAN_CITIES_TOTAL + 1))

        # operation = getUserAction(availableCitiesIds)
    # (2) all capitals of Brazil
    elif operation == 2:
        print('Loading data...')

        data = w.getWeatherData(w.c.CONST_BRAZILIAN_STATE_CAPITAL, w.c.CONST_CITY_WEATHER_BASE_URL)

        print('Your data is ready! What do you want to do?\n(1) - Print\n(2) - Export CSV')

        reportOption = getUserAction([1, 2])

        # data list operations:
        # (1) print in terminal
        if reportOption == 1:
            w.printWeatherData(data)
            print('Completed successfully.\n\n')
        # (2) export to CSV
        else:
            w.getCSVReport(data)
            print('Sucessfully exported.\n\n')
    # (3) Exit program
    else:
        print('Bye.')
        break
