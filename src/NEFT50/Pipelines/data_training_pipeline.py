from src.NEFT50.Config import ConfigurationManager
from src.NEFT50.Components.Data_Modelling import ModelTraining
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
import os,sys
from src.NEFT50.Components.Data_transformation import DataTransformation

class ModelTrainingPipeline():
    def __init__(self):
        pass
    
    def main(self):

        #step6) update the pipeline file
        try:
            cm = ConfigurationManager() #object of configuration manager class
            
            #creating an object of dataclasses
            data_transform_config = cm.get_data_transformation_config()
            model_config = cm.get_model_training_config()

            #creating an object of datatransformation class
            dt = DataTransformation(transformconfig=data_transform_config)

            dt.get_data_transformation()

            train_array,test_array = dt.initiate_data_transformation()

            #creating an object of ModelTraining clas
            mt = ModelTraining(model_config)
            mt.initiate_model_training(
                train_numpy_array=train_array,
                test_numpy_array=test_array,
            )


        except Exception as e:
            raise CustomException(e,sys)

