from django.core.management.base import BaseCommand
from django.conf import settings
import importlib
import inspect

class Command(BaseCommand):
    help = 'Check Django API project installation and model/serializer implementations.'

    def handle(self, *args, **kwargs):
        self.check_django()
        self.check_rest_framework_installed()
        self.check_models()
        self.check_serializers()

    def check_django(self):
        try:
            import django
            self.stdout.write(self.style.SUCCESS(f"Django version: {django.get_version()}"))
        except ImportError:
            self.stdout.write(self.style.ERROR("Django is not installed!"))

    def check_rest_framework_installed(self):
        if 'rest_framework' in settings.INSTALLED_APPS:
            self.stdout.write(self.style.SUCCESS("'rest_framework' is in INSTALLED_APPS"))
        else:
            self.stdout.write(self.style.ERROR("'rest_framework' is NOT in INSTALLED_APPS"))

    def check_models(self):
        try:
            api_models = importlib.import_module('api.models')
        except ImportError:
            self.stdout.write(self.style.ERROR("Cannot import 'api.models'"))
            return

        # Check if Author and Book classes exist
        models_to_check = {
            'Author': ['name'],
            'Book': ['title', 'publication_year', 'author']
        }
        for model_name, required_fields in models_to_check.items():
            model_class = getattr(api_models, model_name, None)
            if not model_class:
                self.stdout.write(self.style.ERROR(f"Model '{model_name}' NOT found in api.models"))
                continue
            self.stdout.write(self.style.SUCCESS(f"Model '{model_name}' found."))

            # Check required fields exist as model attributes
            model_fields = [f.name for f in model_class._meta.get_fields()]
            missing_fields = [f for f in required_fields if f not in model_fields]
            if missing_fields:
                self.stdout.write(self.style.ERROR(f"Model '{model_name}' is missing fields: {missing_fields}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Model '{model_name}' has all required fields."))

    def check_serializers(self):
        try:
            api_serializers = importlib.import_module('api.serializers')
        except ImportError:
            self.stdout.write(self.style.ERROR("Cannot import 'api.serializers'"))
            return

        serializers_to_check = ['BookSerializer', 'AuthorSerializer']
        for serializer_name in serializers_to_check:
            serializer_class = getattr(api_serializers, serializer_name, None)
            if not serializer_class:
                self.stdout.write(self.style.ERROR(f"Serializer '{serializer_name}' NOT found in api.serializers"))
                continue
            self.stdout.write(self.style.SUCCESS(f"Serializer '{serializer_name}' found."))

            # Check if serializer_class subclasses rest_framework.serializers.ModelSerializer
            base_classes = [base.__name__ for base in inspect.getmro(serializer_class)]
            if 'ModelSerializer' in base_classes:
                self.stdout.write(self.style.SUCCESS(f"Serializer '{serializer_name}' is a ModelSerializer."))
            else:
                self.stdout.write(self.style.WARNING(f"Serializer '{serializer_name}' does NOT subclass ModelSerializer."))

