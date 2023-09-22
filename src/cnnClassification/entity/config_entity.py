# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:27:45 2023

@author: ElaheMsvi
"""

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir:Path
    source_URL :str 
    local_data_file :Path
    unzip_dir: Path
    
