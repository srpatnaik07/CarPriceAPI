from django.urls import path
from .views import CarPricePrediction

urlpatterns = [
    path('price/',CarPricePrediction.as_view(),name='Car_Price')
]