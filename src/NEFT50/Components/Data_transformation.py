import pandas as pd,numpy as np,sklearn
from sklearn.pipeline import Pipeline #this class we used to create pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer #to fill null value
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
from sklearn.base import BaseEstimator,TransformerMixin
from src.NEFT50.loggers import logger
from src.NEFT50.Exception import CustomException
from src.NEFT50.Entity import DataTransformationConfig
import os,sys
from src.NEFT50.Utils import Save_object
from pathlib import Path




#step-5) updating the component file of Datatransformation and initializing the class variable as instance variance
class DataTransformation():
    def __init__(self,transformconfig:DataTransformationConfig):
        self.transformconfig = transformconfig #this value we used in our datatransformation stage mei

    def get_data_transformation(self):
        #In this file we create preprocessor object which is futhure used to transformation
        df = pd.read_csv(os.path.join(self.transformconfig.csv_dir_path,"train.csv"))
        
        target_column_name = "target"

        #selecting input and output variable
        x = df[['open', 'high', 'low', 'close', 'volume']]
        y = df[target_column_name]

        #selecting object and numeric column from input variable
        num_feature_lst = x.select_dtypes(exclude='object').columns.to_list()
        cat_feature_lst = x.select_dtypes(include='object').columns.to_list()

        logger.info(f"Numeric column from input feature\n%s",num_feature_lst)
        logger.info(f"Categorical column from input feature\n%s",cat_feature_lst)

        #creating numeric pipeline by using Pipeline class
        numeric_pipeline = Pipeline(steps=[
            ("imputer",SimpleImputer(strategy="median")),#filling the numeric featuere will median
            ("scaling",StandardScaler(with_mean=False))
        ])
        logger.info(f"Numeric Pipeline feature\n%s",numeric_pipeline)

        #creating categorical pipeline by using Pipeline class
        categorical_pipeline = Pipeline(steps=[
            ("imputer",SimpleImputer(strategy="most_frequent")),#filling the categorical feature
            ("onehot",OneHotEncoder(handle_unknown="ignore"))
        ])
        logger.info(f"Categorical Pipeline feature\n%s",categorical_pipeline)

        #combining both pipelien using columntransformer class
        preprocessor = ColumnTransformer(transformers=[
            ("num_pipeline",numeric_pipeline,num_feature_lst),
            ("cat_pipeline",categorical_pipeline,cat_feature_lst)
        ])

        # #now saving the object into artifacts folder
        # save_object(file=self.transformconfig.save_obj_dirpath,obj=preprocessor)

        return preprocessor

    def initiate_data_transformation(self):
        logger.info('Reading train and test Data Using Pandas Library')
        train_data = pd.read_csv(os.path.join(self.transformconfig.csv_dir_path,"train.csv"))
        test_data = pd.read_csv(os.path.join(self.transformconfig.csv_dir_path,"test.csv"))
        
        
        # Extract target column name
        target_column_name = "target"

        #selecting input and output variable from both train,test df object
        train_input_feature = train_data.drop(target_column_name,axis=1)
        train_output_feature = train_data[target_column_name]

        test_input_feature = test_data.drop(target_column_name,axis=1)
        test_output_feature = test_data[target_column_name]

        #calling the preprocessor object
        preprocessor_obj = self.get_data_transformation()

        #now saving the object into artifacts folder
        Save_object(filepath=Path(self.transformconfig.save_obj_dirpath),object=preprocessor_obj)

        #applying this preprocessor object to input variable only for both train and test df object
        input_feature_train_array  = preprocessor_obj.fit_transform(train_input_feature) #changes to 2d numpy array
        input_feature_test_array  = preprocessor_obj.transform(test_input_feature)  #changes to 2d numpy array

        logger.info('Combining  input feature train array with train_data_output_feature---->to get train_numpy_array')
        train_numpy_array = np.c_[input_feature_train_array,np.array(train_output_feature)]
        test_numpy_array = np.c_[input_feature_test_array,np.array(test_output_feature)]

        return(
            train_numpy_array,
            test_numpy_array
        )