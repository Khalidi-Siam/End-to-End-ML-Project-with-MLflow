import pandas as pd
from mlProject.exception import CustomException
from mlProject.entity.config_entity import DataValidationConfig
import sys

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)

            # actual columns in data
            data_cols = list(data.columns)

            expected_schema = self.config.all_schema

            validation_status = True

            # 1. Check if all expected columns exist
            for col in expected_schema.keys():
                if col not in data_cols:
                    validation_status = False
                    break

            # 2. Check if extra columns exist in data
            if validation_status:
                for col in data_cols:
                    if col not in expected_schema:
                        validation_status = False
                        break

            # 3. Check datatype match
            if validation_status:
                for col, expected_dtype in expected_schema.items():
                    actual_dtype = str(data[col].dtype)

                    if actual_dtype != str(expected_dtype):
                        validation_status = False
                        break

            # Write status once
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise CustomException(e, sys)