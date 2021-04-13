import csv
import os

from django.shortcuts import render

from app import settings


def inflation_view(request):
    template_name = 'app/inflation.html'

    # чтение csv-файла и заполнение контекста
    with open(os.path.join(settings.BASE_DIR, 'inflation_russia.csv'), encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        context = [item for item in reader]

    return render(request, template_name, {'keys': context[0], 'content': context})
