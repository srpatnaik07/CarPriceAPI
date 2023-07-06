from django.shortcuts import render
import numpy as np
from .apps import ApiConfig
from rest_framework.views import Response
from rest_framework.views import APIView
import pandas as pd

# Create your views here.
class CarPricePrediction(APIView):
    def post(self, request):
        data = request.data

        # Load the trained model
        model = ApiConfig.model

        # Preprocess the input data
        fuel_type_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
        seller_type_map = {'Dealer': 0, 'Individual': 1}
        transmission_map = {'Manual': 0, 'Automatic': 1}

        fuel_type = data.get('Fuel_Type')
        seller_type = data.get('Seller_Type')
        transmission = data.get('Transmission')

        fuel_type_encoded = fuel_type_map.get(fuel_type)
        seller_type_encoded = seller_type_map.get(seller_type)
        transmission_encoded = transmission_map.get(transmission)

        # Perform predictions
        year = int(data.get('Year'))
        present_price = float(data.get('Present_Price'))
        kms_driven = int(data.get('Kms_Driven'))
        owner = int(data.get('Owner'))

        age = 2023 - year

        features = {
            'Present_Price': [present_price],
            'Kms_Driven': [kms_driven],
            'Fuel_Type': [fuel_type_encoded],
            'Seller_Type': [seller_type_encoded],
            'Transmission': [transmission_encoded],
            'Owner': [owner],
            'Age': [age]
        }

        X = pd.DataFrame(features)
        predictions = model.predict(X)

        # Prepare the response
        response_data = {'predictions': predictions.tolist()}

        return Response(response_data)
