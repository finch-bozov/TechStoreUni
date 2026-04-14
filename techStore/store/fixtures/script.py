import os
import sys
import django

# add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techStore.settings')

django.setup()

from django.core.management import call_command

with open('products.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'store.Product', indent=4, stdout=f)