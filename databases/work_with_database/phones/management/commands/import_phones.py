import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    help = "Saves phone's data to db from csv file"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')
            # пропускаем заголовок
            # next(phone_reader)

            for line in phone_reader:
                Phone.objects.create(
                    name=line['name'],
                    image=line['image'],
                    price=line['price'],
                    release_date=line['release_date'],
                    lte_exists=line['lte_exists'],
                    slug=slugify(line['name'])
                )
