from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request, page=1):
    current_page = page
    next_page_url = reverse('bus_stations', kwargs={'page': current_page + 1})
    prev_page_url = reverse('bus_stations', kwargs={'page': current_page - 1})
    return render(request, 'index.html', context={
        'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'},
                         {'Name': 'другое название', 'Street': 'другая улица', 'District': 'другой район'}],
        'current_page': current_page,
        'prev_page_url': prev_page_url if current_page > 1 else None,
        'next_page_url': next_page_url,
    })

