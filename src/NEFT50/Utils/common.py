#Utils Provide Functionality To Enitre Application!!
import os,sys
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
from dotenv import load_dotenv
from pathlib import Path
import yaml
import joblib
import json
import dill
from box import ConfigBox
from typing import Any



#creating a function to read the yaml file--->rtn result to ConfigBox Dict
def read_yaml_file(filepath: Path):
    try:
        logger.info(f'Reading the YAML file {filepath}')
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
            print(data)
            logger.info(f'YAML file read successfully: {filepath}')
            return ConfigBox(data)

    except Exception as e:
        raise CustomException(e, sys)
    

#Creating a Function to Create Directories
def Create_Directory(path_to_directories:list,verbose=True):
    try:
        logger.info(f'Creating Directory')
        for filepath in path_to_directories:
            if not os.path.exists(filepath):
                os.makedirs(filepath,exist_ok=True)
                logger.info(f'Directory Created at {filepath}')
    except Exception as e:
        raise CustomException(e,sys)
    
    
def Save_object(filepath,object):
    logger.info('Here in Utils we r Creating Save object Function will Save model and preprocessor files to artifacts Folder')
    try:
        logger.info('Now Checking Filepath Exist or not')
        if not os.path.exists('artifacts'):
            os.makedirs('artifacts',exist_ok=True)
        with open(filepath,'wb') as file:
            dill.dump(object,file)
        logger.info('Object Save Into Artfacts Folder')
    except Exception as e:
        raise CustomException(e,sys)