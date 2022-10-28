import requests
import re
from bs4 import BeautifulSoup

def request_weather(city):

    if city == 'Москва':
        city = 'moscow'
    if city == 'Санкт-Петербург':
        city = 'saint_petersburg'
    if city  ==  'Новосибирск':
        city = 'novosibirsk'

    weather = f'https://world-weather.ru/pogoda/russia/{city}/'

    responce = requests.get(weather).text
    soup = BeautifulSoup(responce, 'lxml')
    block = soup.find('div', id= "weather-now-number")
    description = soup.find('div', id='weather-now-description')
    return block.text



def request_weather_description(city):

    if city == 'Москва':
        city = 'moscow'
    if city == 'Санкт-Петербург':
        city = 'saint_petersburg'
    if city  ==  'Новосибирск':
        city = 'novosibirsk'

    weather = f'https://world-weather.ru/pogoda/russia/{city}/'

    responce = requests.get(weather).text
    soup = BeautifulSoup(responce, 'lxml')

    description = soup.find('div', id='weather-now-description')

    return description.text


def sun(city):

    if city == 'Москва':
        city = 'moscow'
    if city == 'Санкт-Петербург':
        city = 'saint_petersburg'
    if city  ==  'Новосибирск':
        city = 'novosibirsk'

    weather = f'https://world-weather.ru/pogoda/russia/{city}/'

    responce = requests.get(weather).text
    soup = BeautifulSoup(responce, 'lxml')

    sun = soup.find('ul', class_='sun')

    return sun.text



gorod = input('Enter a city: ')
print(f'Температура в городе {gorod} - {request_weather(gorod)}, {request_weather_description(gorod)}, {sun(gorod)}')
