import csv

from django.core.management.base import BaseCommand
from django.http import HttpResponse

from django.utils.text import slugify
from phones.models import Phone





class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        print(phones)
        for row in phones:
                phone = Phone(name=row['name'], price=row['price'],image=row['image'],release_date=row['release_date'], lte_existing=row['lte_exists'],slug=slugify(row['name']))
                phone.save()

        return HttpResponse('Данные записаны')

