from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City
from .forms import City_Form

# Create your views here.
def weather(request):
    cities=City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q=kochi&units=imperial&appid=YOUR-API-KEY'
    if request.method=='POST':
        form=City_Form(request.POST)
        form.save()
    form = City_Form()
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)

        context={'weather_data': weather_data, 'form' : form}
