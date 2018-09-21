import requests
from bs4 import BeautifulSoup

weatherSearchUrl = "https://www.climatempo.com.br/previsao-do-tempo/cidade/2710"

request = requests.get(weatherSearchUrl)

soup = BeautifulSoup(request.content)

city = soup.find(id='momento-localidade').text
temp = soup.find(id='momento-temperatura').text
cond = soup.find(id='momento-condicao').text
feel = soup.find(id='momento-sensacao').text
humidity = soup.find(id='momento-humidade').text
pressure = soup.find(id='momento-pressao').text
wind = soup.find(id='momento-vento').text.replace('\n', '').replace(' ', '')

print(city, temp, cond, feel, humidity, pressure, wind)
