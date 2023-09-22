# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:04:44 2023

@author: ElaheMsvi
"""

from cnnClassification import logger
from cnnClassification.pipeline.stage_01_data_ingestion  import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx=====x")        
except Exception as e:
    logger.exception(e)
    raise e
        
