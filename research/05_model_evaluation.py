# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 20:49:54 2023

@author: ElaheMsvi
"""

import os
os.chdir('../')

from dataclasses import dataclass
from pathlib import Path

import tensorflow as tf

model = tf.keras.models.load_model('artifacts/training/model.h5')

@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model : Path 
    training_data : Path 
    all_params : dict
    params_image_size :list 
    params_bach_size :  int
    
    
from cnnClassification.constants import *
from cnnClassification.utils.common import read_yaml, create_directories, save_json

class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
        
        
    def get_validation_config(self)->EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model=Path('artifacts/training/model.h5'),
            training_data=Path('artifacts/data_ingestion/Chicken-fecal-images'),
            all_params=self.params,
            params_bach_size= self.params.BATCH_SIZE,
            params_image_size = self.params.IMAGE_SIZE
            )
        return eval_config
    
# %%
from urllib.parse import urlparse

# %%
class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size= self.config.params_image_size[:-1],
            batch_size  =self.config.params_bach_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = model.evaluate(self.valid_generator)

    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    
# %%
try:
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()

except Exception as e:
   raise e

# %%


    



