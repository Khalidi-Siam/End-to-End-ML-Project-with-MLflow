from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transfromation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from mlProject.exception import CustomException
from mlProject.logger import logging
import sys

STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = "Data Validation Stage"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = "Data Transformation Stage"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = "Model Trainer Stage"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = "Model Evaluation Stage"
try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)
