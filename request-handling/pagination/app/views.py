import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from app import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request, page_number=1):
    chunk = 10

    # Так как файл относительно не большой - читаем целиком
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        paginator = Paginator(list(iter(reader)), chunk)

    page = paginator.get_page(page_number)

    if page.has_next():
        next_page_url = reverse('bus_stations', kwargs={'page_number': page.next_page_number()})
    else:
        next_page_url = None

    if page.has_previous():
        prev_page_url = reverse('bus_stations', kwargs={'page_number': page.previous_page_number()})
    else:
        prev_page_url = None

    return render(request, 'index.html', context={
        'bus_stations': page.object_list,
        'current_page': page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

