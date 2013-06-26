from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class CreateDBError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Command(BaseCommand):
    args = '<json file that will create initial database>'
    help = 'Create Database'

    def handle(self, *args, **options):
        ## 1st load our json file
        print("creating database...")

