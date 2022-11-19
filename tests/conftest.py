from pytest_factoryboy import register
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson28.settings')
import django
django.setup()
from factories import AdFactory, CategoryFactory, UserFactory

pytest_plugins = "tests.fixtures"


register(AdFactory)
register(CategoryFactory)
register(UserFactory)
