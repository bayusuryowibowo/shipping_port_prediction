from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from ..constants.settings import JUPYTER_HOST
from ..exception import handle_request_exception
from ..services.shipping_port_service import get_data, translate_prediction


@api_view(['POST'])
def train_model(request):
  data = get_data()  # Fetch data from PostgreSQL
  try:
    response = requests.post(f'{JUPYTER_HOST}/train', json=data)  # Mengirim to AI
    response.raise_for_status()
  except requests.RequestException as e:
    return handle_request_exception(e)
  return Response(response.json())

@api_view(['POST'])
def predict(request):
  payload = request.data  # Data for prediction from API
  try:
    # Mengirim permintaan HTTP POST ke AI
    response = requests.post(f'{JUPYTER_HOST}/predict', json=payload)
    response.raise_for_status()
    result = response.json()
  except requests.RequestException as e:
    return handle_request_exception(e)

  prediction = result.get('prediction')
  human_readable_prediction = translate_prediction(prediction)
  return Response({'prediction': human_readable_prediction})
