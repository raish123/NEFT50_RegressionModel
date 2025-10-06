import pandas as pd
from sklearn.model_selection import train_test_split
from src.NEFT50.Entity import DataIngestionConfig
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
import os,sys


#step5)update the components files!!! in this file 
class DataIngestion():
    #constructor method initialize the class variable to object
    def __init__(self,ingestionconfig:DataIngestionConfig):
        self.ingestionconfig = ingestionconfig
    
    def train_test_data(self):
        raw_data = self.ingestionconfig.raw_file_path

        logger.info(f"Loading the csv file {raw_data}")

        df_raw = pd.read_csv(raw_data)

        logger.info(f"splitting the Raw dataset")

        train_df,test_df = train_test_split(df_raw,test_size=0.2,random_state=42)

        #saving training and testing data
        train_df.to_csv(os.path.join(self.ingestionconfig.train_test_path,"train.csv"))
        test_df.to_csv(os.path.join(self.ingestionconfig.train_test_path,"test.csv"))

