# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 21:46:56 2023

@author: ElaheMsvi
"""
from cnnClassification.config.configuration import ConfigurationManager
from cnnClassification.component.evaluation import Evaluation
from pathlib import Path
from cnnClassification import logger

STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            