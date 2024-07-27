import csv
import os
import django
from decimal import Decimal, InvalidOperation

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from companies.models import Company

# Path to the CSV file
csv_file_path = '/Users/krxshi/Downloads/full_stack_enginering_assignment/company_data.csv'

with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Handle revenue field
        revenue = row.get('revenue', '').strip()
        if revenue == '':
            revenue = 0
        else:
            try:
                revenue = Decimal(revenue)
            except InvalidOperation:
                revenue = 0  # Default to 0 if the value is not a valid decimal

        Company.objects.update_or_create(
            id=row['id'],
            defaults={
                'entity': row['entity'],
                'sector': row['sector'],
                'email': row['email'],
                'incorporation': row['incorporation'],
                'address': row['address'],
                'revenue': revenue,
                'website': row['website'],
                'is_verified': row['is_verified'].lower() in ('true', '1', 'yes')
            }
        )
