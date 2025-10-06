from src.NEFT50.Utils import Create_Directory,read_yaml_file
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
from src.NEFT50.Constants import CONFIG_FILEPATH,PARAM_FILEPATH
import os,sys
from src.NEFT50.Entity import DataIngestionConfig,DataTransformationConfig,ModelTrainingConfig



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


    def get_data_transformation_config(self):
        #creating local variable which was used inside this method
        transform = self.config.data_transformation

        #creating root directory in artifacts folder for datatransformation
        Create_Directory([transform.root_dir_path]) #create artifacts/data_transformation folder

        #creating an object &
        #assigining the value to DataTransformationConfig class variable and taking rtn as function
        data_transformation_config = DataTransformationConfig(
            root_dir_path=transform.root_dir_path,
            save_obj_dirpath=transform.save_obj_dirpath,
            csv_dir_path=transform.csv_dir_path,
           
        )

        return data_transformation_config
    
    #another method we used to get model training config!!!
    def get_model_training_config(self) ->ModelTrainingConfig:
        #initializing the local variable which is used inside this method only
        config = self.config.model_training
      

        #creating directory artifacts/model_training
        Create_Directory([config.root_dir_path])

        #creating an object of class variable and assigning value to parameter and taking rtn as fuctn
        model_training_config = ModelTrainingConfig(
            root_dir_path = config.root_dir_path,
            save_best_model_dirpath=config.save_best_model_dirpath,
     
        )
        return model_training_config