from django.core.management.base import BaseCommand
from django.conf import settings
import importlib
import inspect

class Command(BaseCommand):
    help = 'Verify Django REST Framework project setup, including Django, api app, installed apps, models, and serializers.'

    def handle(self, *args, **kwargs):
        self.check_django()
        self.check_installed_apps()
        self.check_models()
        self.check_serializers()

    def check_django(self):
        try:
            import django
            self.stdout.write(self.style.SUCCESS(f"Django version: {django.get_version()}"))
        except ImportError:
            self.stdout.write(self.style.ERROR("Django is not installed."))

    def check_installed_apps(self):
        # Check if 'api' app is installed
        if 'api' in settings.INSTALLED_APPS:
            self.stdout.write(self.style.SUCCESS("'api' app is in INSTALLED_APPS"))
        else:
            self.stdout.write(self.style.ERROR("'api' app is NOT in INSTALLED_APPS"))

        # Check if rest_framework is installed
        if 'rest_framework' in settings.INSTALLED_APPS:
            self.stdout.write(self.style.SUCCESS("'rest_framework' is in INSTALLED_APPS"))
        else:
            self.stdout.write(self.style.ERROR("'rest_framework' is NOT in INSTALLED_APPS"))

    def check_models(self):
        try:
            models = importlib.import_module('api.models')
        except ImportError:
            self.stdout.write(self.style.ERROR("Cannot import 'api.models'"))
            return

        expected_models = {
            'Author': ['name'],
            'Book': ['title', 'publication_year', 'author'],
        }

        for model_name, fields in expected_models.items():
            model = getattr(models, model_name, None)
            if model is None:
                self.stdout.write(self.style.ERROR(f"Model '{model_name}' not found."))
                continue
            self.stdout.write(self.style.SUCCESS(f"Model '{model_name}' found."))

            model_fields = [f.name for f in model._meta.get_fields()]
            missing_fields = [f for f in fields if f not in model_fields]
            if missing_fields:
                self.stdout.write(self.style.ERROR(f"Model '{model_name}' missing fields: {missing_fields}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Model '{model_name}' has all required fields."))

    def check_serializers(self):
        try:
            serializers = importlib.import_module('api.serializers')
        except ImportError:
            self.stdout.write(self.style.ERROR("Cannot import 'api.serializers'"))
            return

        expected_serializers = ['BookSerializer', 'AuthorSerializer']

        for serializer_name in expected_serializers:
            serializer = getattr(serializers, serializer_name, None)
            if serializer is None:
                self.stdout.write(self.style.ERROR(f"Serializer '{serializer_name}' not found."))
                continue
            self.stdout.write(self.style.SUCCESS(f"Serializer '{serializer_name}' found."))

            bases = [base.__name__ for base in inspect.getmro(serializer)]
            if 'ModelSerializer' in bases:
                self.stdout.write(self.style.SUCCESS(f"Serializer '{serializer_name}' subclasses ModelSerializer."))
            else:
                self.stdout.write(self.style.WARNING(f"Serializer '{serializer_name}' does NOT subclass ModelSerializer."))
