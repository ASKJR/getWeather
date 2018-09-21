import requests
from bs4 import BeautifulSoup

CONST_LOCALITY_ID = 'momento-localidade'
CONST_TEMPERATURE_ID = 'momento-temperatura'
CONST_CONDITION_ID = 'momento-condicao'
CONST_REAL_FEEL_ID = 'momento-sensacao'
CONST_HUMIDITY_ID = 'momento-humidade'
CONST_PRESSURE_ID = 'momento-pressao'
CONST_WIND_SPEED_ID = 'momento-vento'
CONST_BRAZILIAN_CITIES_TOTAL = 5570
CONST_BRAZILIAN_STATE_CAPITAL = ['6', '8', '39', '25', '56', '60', '61', '84', '88', '94', '218', '212', '107', '232', '256', '271', '259', '264', '321', '334', '363', '343', '347', '377', '558', '384', '593']


def getCity():
    return soup.find(id=CONST_LOCALITY_ID).text.split('-')[0].strip()


def getState():
    return soup.find(id=CONST_LOCALITY_ID).text.split('-')[1].strip()


def getTemperature():
    return soup.find(id=CONST_TEMPERATURE_ID).text.strip()


def getWeatherCondition():
    return soup.find(id=CONST_CONDITION_ID).text.strip()


def getRealFeel():
    return soup.find(id=CONST_REAL_FEEL_ID).text.strip()


def getHumidity():
    return soup.find(id=CONST_HUMIDITY_ID).text.strip()


def getPressure():
    return soup.find(id=CONST_PRESSURE_ID).text


def getWindSpeed():
    return soup.find(id=CONST_WIND_SPEED_ID).text.replace('\n', '').replace(' ', '')


for capitalID in CONST_BRAZILIAN_STATE_CAPITAL:
    weatherSearchUrl = "https://www.climatempo.com.br/previsao-do-tempo/cidade/" + capitalID

    request = requests.get(weatherSearchUrl)

    soup = BeautifulSoup(request.content, 'html.parser')

    city = getCity()
    state = getState()
    temp = getTemperature()
    cond = getWeatherCondition()
    feel = getRealFeel()
    humidity = getHumidity()
    pressure = getPressure()
    wind = getWindSpeed()

    print(city, state, temp, cond, feel, humidity, pressure, wind)
