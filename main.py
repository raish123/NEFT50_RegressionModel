from src.NEFT50.Pipelines.data_ingestion_pipeline import DataIngestionPipeline
from src.NEFT50.Pipelines.data_training_pipeline import ModelTrainingPipeline
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
import os,sys

stage_name = "Data Ingestion"

try:
    logger.info(f">>>{stage_name} started <<<<")
    #creating an object of DataIngestionTraining class
    dit = DataIngestionPipeline()
    dit.main()
    logger.info(f">>>{stage_name} stopped <<<<")

except Exception as e:
    raise CustomException(e,sys)

print('*'*100)

stage_name2 = "Data Transformation and Modelling performing"

try:
    logger.info(f">>>{stage_name2} started <<<<")
    #creating an object of DataIngestionTraining class
    dt = ModelTrainingPipeline()
    dt.main()
    logger.info(f">>>{stage_name2} stopped <<<<")

except Exception as e:
    raise CustomException(e,sys) 