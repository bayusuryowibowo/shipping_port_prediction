import os
import csv
from django.core.management.base import BaseCommand
from app.models import ShippingPort

class Command(BaseCommand):
  help = 'Import shipping port data from CSV'

  def handle(self, *args, **kwargs):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, '../../data/shipping_port.csv')
    file_path = os.path.abspath(file_path)

    if not os.path.exists(file_path):
      self.stderr.write(f'Error: The file {file_path} does not exist.')
      return

    with open(file_path, mode='r') as file:
      reader = csv.DictReader(file)
      for row in reader:
        ShippingPort.objects.update_or_create(
          product_type=row['Product type'],
          order_quantities=int(row['Order quantities']),
          shipping_carriers=row['Shipping carriers'],
          shipping_costs=float(row['Shipping costs']),
          origin=row['Origin'],
          inspection_results=row['Inspection results'],
          defect_rates=float(row['Defect rates']),
          routes=row['Routes'],
          eta=row['ETA']
        )

    self.stdout.write(self.style.SUCCESS('Data imported successfully'))