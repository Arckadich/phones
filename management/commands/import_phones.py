import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    help = 'Imports phones from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='The CSV file to import')

    def handle(self, *args, **options):
        file_path = options['file']

        with open(file_path, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_obj = Phone(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists']
            )
            phone_obj.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported phones from CSV file'))
