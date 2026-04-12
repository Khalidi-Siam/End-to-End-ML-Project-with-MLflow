from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject.exception import CustomException
import sys

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train_model()
        except Exception as e:
            raise CustomException(e, sys)