from django.core.management.base import BaseCommand
import django
import rest_framework

class Command(BaseCommand):
    help = 'Check Django and DRF installation'

    def handle(self, *args, **kwargs):
        self.stdout.write(f"Django version: {django.get_version()}")
        self.stdout.write(f"DRF version: {rest_framework.VERSION}")
