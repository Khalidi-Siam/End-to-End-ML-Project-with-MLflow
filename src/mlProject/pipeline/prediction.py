import joblib 
from pathlib import Path
from mlProject.exception import CustomException
import sys

class PredictionPipeline:
    def __init__(self):
        try:
            self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction