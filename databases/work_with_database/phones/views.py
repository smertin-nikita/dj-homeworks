from django.shortcuts import render, redirect
from django.urls import reverse

from phones.models import Phone


def index(request):
    return redirect(reverse('catalog'))


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    phones = list(Phone.objects.all())
    if sort:
        if sort == 'name':
            phones = list(Phone.objects.order_by('name'))
        if sort == 'min_price':
            phones = list(Phone.objects.order_by('price'))
        if sort == 'max_price':
            phones = list(Phone.objects.order_by('-price'))

    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
