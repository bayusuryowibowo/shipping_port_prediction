from django.db import models

# Create your models here.
class ShippingPort(models.Model):
  class Meta:
    db_table = 'shipping_port'

  PRODUCT_TYPE_CHOICES = [
    ('cosmetics', 'Cosmetics'),
    ('skincare', 'Skincare'),
    ('haircare', 'Haircare'),
  ]

  SHIPPING_CARRIER_CHOICES = [
    ('Carrier A', 'Carrier A'),
    ('Carrier B', 'Carrier B'),
    ('Carrier C', 'Carrier C'),
  ]

  INSPECTION_RESULT_CHOICES = [
    ('Pass', 'Pass'),
    ('Fail', 'Fail'),
    ('Pending', 'Pending'),
  ]

  ROUTE_CHOICES = [
    ('Route A', 'Route A'),
    ('Route B', 'Route B'),
    ('Route C', 'Route C'),
  ]

  ETA_CHOICES = [
    ('On time', 'On time'),
    ('Delay', 'Delay'),
  ]

  product_type = models.CharField(max_length=50, choices=PRODUCT_TYPE_CHOICES)
  order_quantities = models.PositiveIntegerField()
  shipping_carriers = models.CharField(max_length=50, choices=SHIPPING_CARRIER_CHOICES)
  shipping_costs = models.FloatField()
  origin = models.CharField(max_length=100)
  inspection_results = models.CharField(max_length=50, choices=INSPECTION_RESULT_CHOICES)
  defect_rates = models.FloatField()
  routes = models.CharField(max_length=50, choices=ROUTE_CHOICES)
  eta = models.CharField(max_length=50, choices=ETA_CHOICES)

  def __str__(self):
    return f'{self.product_type} - {self.order_quantities} units'