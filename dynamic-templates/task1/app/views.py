import csv
import os

from django.shortcuts import render

from app import settings


def inflation_view(request):
    template_name = 'app/inflation.html'

    # чтение csv-файла и заполнение контекста
    with open(os.path.join(settings.BASE_DIR, 'inflation_russia.csc')) as csvfile:
        context = csv.DictReader(csvfile)

    return render(request, template_name, context)
