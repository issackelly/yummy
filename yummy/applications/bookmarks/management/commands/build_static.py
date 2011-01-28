from django.core.management.base import BaseCommand, CommandError
from optparse import make_option


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
            make_option('--no-input',
                action='store_true',
                dest='delete',
                default=False,
                help='Delete poll instead of closing it'),
            )

    def handle(self, *args, **options):
        return