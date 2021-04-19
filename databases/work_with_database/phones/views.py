from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort:
        if sort == 'name':
            pass
        if sort == 'min_price':
            pass

    template = 'catalog.html'
    context = {'phones': list(Phone.objects.all())}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
