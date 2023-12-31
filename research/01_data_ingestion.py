# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:10:43 2023

@author: ElaheMsvi
"""

import os 

# %pwd

# os.chdir("../")

# %pwd

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir:Path
    source_URL :str 
    local_data_file :Path
    unzip_dir: Path
    
    
from cnnClassification.constants import *
from cnnClassification.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir = config.unzip_dir)
        
        return data_ingestion_config
        
    def prepare_base_model_config(self)->PrepareBaseModelConfig:
        config =self.config.prepare_base_model
        
        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfig(
        root_dir = Path(config.root_dir),
        base_model_path = Path(config.base_model_path),
        updated_base_model_path = Path(config.updated_base_model_path),
        params_image_size = self.params.IMAGE_SIZE,
        AUGMENTATION : True
        IMAGE_SIZE : [224,224, 3]
        BATCH_SIZE : 16
        INCLUDE_TOP : False
        EPOCHS:1
        CLASSES : 2
        WEGHTS:imagenet
        LEARNING_RATE:.01

        
    
    
        )
        return prepare_base_model_config

import os
import urllib.request as request

import zipfile
from cnnClassification import logger
from cnnClassification.utils.common import get_size



class DataIngestion:
    def __init__(self , config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
except Exception as e:
    raise e            
        
        
        
        