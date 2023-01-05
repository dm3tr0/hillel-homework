from django.core.management.base import BaseCommand, CommandParser
import csv
from project.settings import BASE_DIR 
from movies.models import Movie

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
                    models=Movie(id=line[0], title_type=line[1], name=line[2], adult=line[4], year=line[5], genre=line[-1])
                    models.save()