import requests
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import City
from .forms import CityForm


def index(request):
    appid = '02da55a6c9993658bf9c619a92b97a58'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()
    b = []
    if request.method == 'POST':
        form = CityForm(request.POST)
        namer = request.POST['name']
        p = requests.get(url.format(namer)).json()

        for city in cities:
            b.append(city.name)

        if p['cod'] == 200:

            if namer not in b :
                b.append(namer)
                form.save()


    cities = City.objects.all()

    form = CityForm()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
