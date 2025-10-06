from src.NEFT50.Utils import Create_Directory,read_yaml_file
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
from src.NEFT50.Constants import CONFIG_FILEPATH,PARAM_FILEPATH
import os,sys
from src.NEFT50.Entity import DataIngestionConfig



#step4)update the configurationmanager file which was present in src/config/configuration.py
#In this file we are reading yaml file ,create directory and also 
#assigning the value to the class variable and taking rtn as function

class ConfigurationManager():
    #initializing the instance variable 
    def __init__(self,config_filepath=CONFIG_FILEPATH,param_filepath=PARAM_FILEPATH):
        #reading the yaml file
        self.config = read_yaml_file(config_filepath) #rtn value as configdictatonary
        self.param = read_yaml_file(param_filepath) #rtn value as configdictatonary
        print(self.config)

        #creating main directory in project structure
        Create_Directory([self.config.artifacts_root]) #it will create artifact directory

    #creating method to initialize value to dataingestion
    def data_ingestion(self) ->DataIngestionConfig:
        #initializing local variable
        config = self.config.data_ingestion #here we r accessing dataingestion block from yaml file

        #creating dataingestion root_dir_path
        Create_Directory([config.root_dir_path])

        #creating an object of DataIngestionConfig class and initialize class variable value to it 
        data_ingestion_config = DataIngestionConfig(
            root_dir_path=config.root_dir_path,
            train_test_path=config.train_test_path,
            raw_file_path = config.raw_file_path
         
        )
        return data_ingestion_config
