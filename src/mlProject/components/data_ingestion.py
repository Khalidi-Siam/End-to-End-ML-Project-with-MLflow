import os
import sys
import urllib.request as request
from zipfile import ZipFile
from mlProject.utils.common import get_size
from mlProject.logger import logging
from mlProject.exception import CustomException
from mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                self.config.source_URL, self.config.local_data_file
            )
            logging.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        '''
        zip_file_path: str
        Extract the zip fine into the data directory
        Function returns None
        '''
        with ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        os.remove(self.config.local_data_file)  