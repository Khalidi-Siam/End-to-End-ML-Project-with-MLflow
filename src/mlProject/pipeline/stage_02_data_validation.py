from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject.exception import CustomException
from mlProject.logger import logging
import sys


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            print(data_validation_config)

            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()

        except Exception as e:
            raise CustomException(e, sys)
        