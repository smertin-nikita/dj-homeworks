import csv

from django.shortcuts import render, redirect
from django.urls import reverse

from app import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request, page=1):
    chunk = 10
    offset = chunk * (page - 1)

    next_page_url = reverse('bus_stations', kwargs={'page': page + 1})
    prev_page_url = reverse('bus_stations', kwargs={'page': page - 1})

    # Так как файл относительно не большой - читаем целиком
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    return render(request, 'index.html', context={
        'bus_stations': data[offset:offset + chunk],
        'current_page': page,
        'prev_page_url': prev_page_url if page > 1 else None,
        'next_page_url': next_page_url,
    })

