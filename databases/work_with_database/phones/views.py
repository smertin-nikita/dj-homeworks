from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    phones = list(Phone.objects.all())

    if sort:
        if sort == 'name':
            phones.sort(key=lambda phone: phone.name)
        if sort == 'min_price':
            phones.sort(key=lambda phone: phone.price)
        if sort == 'max_price':
            phones.sort(key=lambda phone: phone.price, reverse=True)

    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
