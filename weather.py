import requests
from bs4 import BeautifulSoup
import config as c


def setBeautifulSoup():
    c.soup = BeautifulSoup(c.request, 'html.parser')


def getRequestContent(url):
    c.request = requests.get(url).content


def isCityWeatherDataAvailable():
    return c.soup.find(id=c.CONST_WEATHER_BOX_ID)


def getCity():
    return c.soup.find(id=c.CONST_LOCALITY_ID).text.split('-')[0].strip()


def getState():
    return c.soup.find(id=c.CONST_LOCALITY_ID).text.split('-')[1].strip()


def getTemperature():
    return c.soup.find(id=c.CONST_TEMPERATURE_ID).text.strip()


def getWeatherCondition():
    return c.soup.find(id=c.CONST_CONDITION_ID).text.strip()


def getRealFeel():
    return c.soup.find(id=c.CONST_REAL_FEEL_ID).text.strip()


def getHumidity():
    return c.soup.find(id=c.CONST_HUMIDITY_ID).text.strip()


def getPressure():
    return c.soup.find(id=c.CONST_PRESSURE_ID).text


def getWindSpeed():
    return c.soup.find(id=c.CONST_WIND_SPEED_ID).text.replace('\n', '').replace(' ', '')


def getWeatherData(citiesId, requestedUrl):
    weather = []
    for cityId in citiesId:
        getRequestContent(requestedUrl + cityId)
        setBeautifulSoup()
        if isCityWeatherDataAvailable():
            weather.append([getCity(), getState(), getTemperature(), getWeatherCondition(), getRealFeel(), getHumidity(), getPressure(), getWindSpeed()])
    return weather


def getCSVReport(data):
    header = "cidade,estado,temperatura,condicao,sensacao,humidade,pressao,vento\n"
    file = open("weatherData.csv", "w", encoding="utf-8")
    file.write(header)
    for city in data:
        file.write(",".join(city) + "\n")
    file.close()


def printWeatherData(data):
    for city in data:
        print(" ".join(city) + "\n")
