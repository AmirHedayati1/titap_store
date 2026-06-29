import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Seeds the database with dummy data from Mockaroo JSON files'

    def add_arguments(self, parser):
        parser.add_argument('--products', type=str, help='Path to products JSON file')

    def handle(self, *args, **options):
        prod_file = options['products']

        if not prod_file:
            self.stderr.Errorf('Please provide paths to both JSON files using --products')
            return
        
        try:
            with transaction.atomic():
                self.stdout.write(self.style.SUCCESS('Starting Products seeding...'))
                with open(prod_file, 'r', encoding='utf-8') as f:
                    products_data = json.load(f)
                    for item in products_data:
                        category_name = item.get('category_name')
                        category = Category.objects.filter(name=category_name).first()

                        product, created = Product.objects.get_or_create(
                            name=item['name'],
                            defaults={
                                'category': category,
                                'slug': slugify(item['name']),
                                'stock': item['stock'],
                                'price': item['price'],
                                'description': item['description'],
                            }
                        )
                        if created:
                            self.stdout.write(f'Created Product: {product.name}')
                self.stdout.write(self.style.SUCCESS('Successfully seeded all data!'))

        except Exception as e:
            self.stderr.Errorf(f'An error occurred: {e}')