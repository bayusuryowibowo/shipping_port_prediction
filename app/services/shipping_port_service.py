from ..models import ShippingPort


# Service untuk mengambil semua data dari table shipping_port di postgres
def get_data():
  data = ShippingPort.objects.all().values()
  data_list = list(data)
  for item in data_list:
    item['product_type'] = dict(ShippingPort.PRODUCT_TYPE_CHOICES).get(item['product_type'])
    item['shipping_carriers'] = dict(ShippingPort.SHIPPING_CARRIER_CHOICES).get(item['shipping_carriers'])
    item['inspection_results'] = dict(ShippingPort.INSPECTION_RESULT_CHOICES).get(item['inspection_results'])
    item['routes'] = dict(ShippingPort.ROUTE_CHOICES).get(item['routes'])
    item['eta'] = dict(ShippingPort.ETA_CHOICES).get(item['eta'])

  return data_list

def translate_prediction(prediction):
  prediction_map = {
    0: "Delay",
    1: "On time"
  }
  return prediction_map.get(prediction, "Unknown")
