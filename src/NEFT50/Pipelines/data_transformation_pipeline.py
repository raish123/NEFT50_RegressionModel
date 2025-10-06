from src.NEFT50.Config import ConfigurationManager
from src.NEFT50.Components.Data_transformation import DataTransformation
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
import os,sys


class DataTransformationPipeline():
    def __init__(self):
        pass
    
    def main(self):

        #step6)update the training pipeline file
        try:
            #creating an object of configuration manager
            cm = ConfigurationManager()
            data_transform_config = cm.get_data_transformation_config()

            #creating an object of datatransformation class
            dt = DataTransformation(transformconfig=data_transform_config)

            dt.get_data_transformation()

            train_array,test_array = dt.initiate_data_transformation()


        except Exception as e:
            raise CustomException(e,sys)