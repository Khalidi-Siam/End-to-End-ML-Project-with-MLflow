import joblib 
import numpy as np
import pandas as pd
from pathlib import Path
import mlflow
import os
from mlProject.exception import CustomException
import sys

class PredictionPipeline:
    def __init__(self):
        tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
        model_name = "ElasticnetModel"
        
        # Hardcoding the alias to 'best' as requested
        model_alias = "best" 
        
        try:
            if tracking_uri:
                mlflow.set_tracking_uri(tracking_uri)
                print(f"**** Loading model using alias: @{model_alias} ******")
                
                model_uri = f"models:/{model_name}@{model_alias}"
                
                self.model = mlflow.sklearn.load_model(model_uri)
                
            else:
                # If MLFLOW_TRACKING_URI is not set, fallback to loading the model from a local path
                self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction