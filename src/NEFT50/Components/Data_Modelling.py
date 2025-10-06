import os,sys
from pathlib import Path
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
from src.NEFT50.Entity import ModelTrainingConfig
import numpy as np
from src.NEFT50.Utils import Create_Directory,read_yaml_file,Save_object



#step5) update the component file: In this file we create an object for class varibale
#and perform model training task accordingly
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class ModelTraining():
    def __init__(self,modelconfig:ModelTrainingConfig):
        self.modelconfig = modelconfig

    #create kar raha hu method to perform training of model through grid search cv and get best param from it
    def initiate_model_training(self,train_numpy_array,test_numpy_array):

        #now selecting training and testing data from numpy array obj
        x_train, y_train = train_numpy_array[:,:-1],train_numpy_array[:,-1]
        x_test, y_test = test_numpy_array[:,:-1],test_numpy_array[:,-1]

        # Initialize Linear Regression model
        model = LinearRegression()

        # Train model
        model.fit(x_train, y_train)
        logger.info("Model training completed successfully.")
        
        # Make predictions on test set
        y_pred = model.predict(x_test)

        # Evaluate model performance
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        logger.info(f"Linear Regression Performance -> R2: {r2:.4f}, MSE: {mse:.4f}, RMSE: {rmse:.4f}")
        
        # Save model only if performance is acceptable
        if r2 > 0.50:
            Save_object(
                filepath=Path(self.modelconfig.save_best_model_dirpath),
                object=model
            )
            logger.info("Model saved successfully as best model.")
        else:
            logger.warning("Model R² score below threshold (0.50). Not saving the model.")

        