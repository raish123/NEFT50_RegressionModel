from src.NEFT50.Config import ConfigurationManager
from src.NEFT50.Components.Data_ingestion import DataIngestion
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
import os,sys


class DataIngestionPipeline():
    def __init__(self):
        pass
    
    def main(self):

        #step6)update the training pipeline file
        try:
            #creating an object of configurationmanager class
            cm = ConfigurationManager()

            data_ingestion_config = cm.data_ingestion()

            #creating an object of DataIngestion component class
            di = DataIngestion(ingestionconfig = data_ingestion_config)

            di.train_test_data()


        except Exception as e:
            raise CustomException(e,sys)