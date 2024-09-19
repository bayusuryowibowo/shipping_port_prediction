from rest_framework.response import Response
from rest_framework.exceptions import APIException
import requests

class CustomException(APIException):
  status_code = 500
  default_detail = 'A server error occurred.'

  def __init__(self, detail=None, code=None):
    if detail is not None:
      self.detail = detail
    if code is not None:
      self.status_code = code

def handle_request_exception(exc):
  if isinstance(exc, requests.RequestException):
    error_message = str(exc)
    status_code = exc.response.status_code if exc.response is not None else 500
    if exc.response is not None:
      try:
        error_data = exc.response.json()
        error_message = error_data.get('error', 'Unknown error')
      except ValueError:
        error_message = exc.response.text

    clean_error_message = ' '.join(error_message.split())
    return Response({'error': clean_error_message}, status=status_code)

  return Response({'error': 'An unexpected error occurred.'}, status=500)
