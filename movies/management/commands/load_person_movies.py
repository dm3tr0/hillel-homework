from django.core.management.base import BaseCommand, CommandParser
import csv
from project.settings import BASE_DIR 
from movies.models import PersonMovie

class Command(BaseCommand):
    help = 'mayonese on a escaletor'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--file', type=str, help='file directory')

    def handle(self, *args, **options):
        file = options['file']

        if file:
            with open(str(BASE_DIR)+"\\movies\\mdb\\"+file, encoding='utf-8') as dir:
                tsv_file = csv.reader(dir, delimiter="\t")
                for line in tsv_file:
                    models=PersonMovie(mid=line[0], pid=line[2], order=line[1], category=line[3], job=line[4], chars=line[5])
                    models.save()