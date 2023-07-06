from django.apps import AppConfig
import os
from django.conf import settings
import joblib


class ApiConfig(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS,"CarPricePredictionModel.joblib")
    model = joblib.load(MODEL_FILE)
        
