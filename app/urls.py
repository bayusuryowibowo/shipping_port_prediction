from django.urls import path
from .controllers.shipping_port_controller import train_model, predict

urlpatterns = [
    path('train', train_model, name='train_model'),
    path('predict', predict, name='predict'),
]
