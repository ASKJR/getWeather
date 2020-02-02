import requests
from bs4 import BeautifulSoup
import config as c


def setBeautifulSoup():
    c.soup = BeautifulSoup(c.request, 'html.parser')


def getRequestContent(url):
    c.request = requests.get(url).content


def isCityWeatherDataAvailable():
    return c.soup.find("p", class_=c.CONST_CONDITION_CLASS)


def getCity():
    return c.soup.find("span", class_=c.CONST_LOCALITY_CLASS).text.split('-')[0].strip()


def getState():
    return c.soup.find("span", class_=c.CONST_LOCALITY_CLASS).text.split('-')[1].strip()


def getTemperature():
    return c.soup.find(
        "span", class_=c.CONST_TEMPERATURE_CLASS).contents[0].strip()


def getRain():
    return c.soup.find("p", class_=c.CONST_CONDITION_CLASS).text.strip()


def getRealFeel():
    return c.soup.find("span", class_=c.CONST_TEMPERATURE_CLASS).contents[1].contents[1].text + 'º'


def getHumidity():
    return c.soup.find("div", class_=c.CONST_INFO_BOX_CLASS).find_all("p", class_="-gray")[2].text.strip()


def getSunrise():
    return c.soup.find(alt=c.CONST_SUN_RISE_ALT).parent.text.strip()


def getWindSpeed():
    return c.soup.find("div", class_=c.CONST_INFO_BOX_CLASS).find_all("p", class_="-gray")[3].text.strip()


def getWeatherData(citiesId, requestedUrl):
    weather = []
    for cityId in citiesId:
        getRequestContent(requestedUrl + cityId)
        setBeautifulSoup()
        if isCityWeatherDataAvailable():
            weather.append([getCity(), getState(), getTemperature(), getRealFeel(), getRain(), getHumidity(), getWindSpeed(), getSunrise()])
    return weather


def getCSVReport(data):
    header = "cidade,estado,temperatura,sensacao,chuva,umidade,vento,amanhecer\n"
    file = open("weatherData.csv", "w", encoding="utf-8")
    file.write(header)
    for city in data:
        file.write(",".join(city) + "\n")
    file.close()


def printWeatherData(data):
    for city in data:
        print(" ".join(city) + "\n")
