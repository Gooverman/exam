import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = 'a9e27fddc5b3f48f6a43c514ce4738f7'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()  # Instantiate the form

    cities = City.objects.all()
    all_cities = []

    for city_obj in cities:
        city = city_obj.name
        res = requests.get(url.format(city)).json()

        city_info = {
           'city': city,
           'temp': res['main']['temp'],
           'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
