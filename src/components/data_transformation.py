# Handling missing values
# Outliers treatment
# handling Imbalance Data in Dataset
# Converting categorical columns into numerical columns

import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils import save_object


@dataclass
class DataTransformationConfigs:
    preprocess_obj_file_path = os.path.join("artifacts/data_transformation", "preprocess.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfigs()

    def get_data_transformation_obj(self):
        try:
            logging.info(" Data Transformation started ")

            numerical_features = ['age', 'workclass', 'education_num',
                                  'marital_status', 'occupation', 'relationship', 'race', 'sex',
                                  'capital_gain', 'capital_loss', 'hours_per_week', 'native_country']
            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy='median')),
                    ("scaler", StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_features)
            ])

            return preprocessor
        

        except Exception as e:
            raise CustomException (e, sys)
        
    def remove_outliers_IQR(self, df, col):
        try:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)

            iqr = Q3 - Q1
            upper_limit = Q3 + 1.5 * iqr
            lower_limit = Q1 - 1.5 * iqr

            df.loc[(df[col] > upper_limit), col] = upper_limit.astype(df[col].dtype)
            df.loc[(df[col] < lower_limit), col] = lower_limit.astype(df[col].dtype)


            return df
        except Exception as e:
            logging.info("Outlier handling code")
            raise CustomException (e, sys)
    
    def initiate_data_transformation(self, train_path, test_path, some_other_argument=None ):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            numerical_features = ['age', 'workclass', 'education_num',
                                  'marital_status', 'occupation', 'relationship', 'race', 'sex',
                                  'capital_gain', 'capital_loss', 'hours_per_week', 'native_country'] 
            for col in numerical_features:
                self.remove_outliers_IQR(col = col, df = train_data)
            
            logging.info("Outliers capped on train data")

            for col in numerical_features:
                self.remove_outliers_IQR(col = col, df = test_data)
            
            logging.info("Outliers capped on test data")

            preprocess_obj = self.get_data_transformation_obj()

            target_column = "income"
            drop_columns = [target_column]

            logging.info("Splitting train data into Dependent and Independent features")

            input_feature_train_data = train_data.drop(drop_columns, axis=1)
            target_feature_train_data = train_data[target_column]

            logging.info("Splitting test data into Dependent and Independent features")

            input_feature_test_data = test_data.drop(drop_columns, axis=1)
            target_feature_test_data = test_data[target_column]

            # Apply transformation on our train data and test data
            input_train_arr = preprocess_obj.fit_transform(input_feature_train_data)
            input_test_arr = preprocess_obj.transform(input_feature_test_data)

            # Apply Preprocessor object on train and test data
            train_array = np.c_[input_train_arr, np.array(target_feature_train_data)]
            test_array = np.c_[input_test_arr, np.array(target_feature_test_data)]

            save_object(file_path = self.data_transformation_config.preprocess_obj_file_path,
                        obj = preprocess_obj)
            
            return(train_array,
                   test_array,
                   self.data_transformation_config.preprocess_obj_file_path)
        except Exception as e:
            raise CustomException(e, sys)


# This code below is for the categorical data if present in the data set as in our data set we dont have any.        
#           cate_pipeline = Pipeline(
#               steps = [
#                    ("imputer", SimpleImputer(strategy='mode')) ])

