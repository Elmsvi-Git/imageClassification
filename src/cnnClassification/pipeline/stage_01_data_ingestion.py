# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:37:00 2023

@author: ElaheMsvi
"""

from cnnClassification.config.configuration import ConfigurationManager
from cnnClassification.component.data_ingestion import DataIngestion
from cnnClassification import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':

    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=====x")        
    except Exception as e:
        logger.exception(e)
        raise e
        
        
        
        
