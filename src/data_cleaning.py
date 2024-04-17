import logging 
from abc import ABC, abstractmethod
from typing import Union

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataStrategy(ABC):
    """
    Abstract class definined strategy for handling data
    """
    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass

class DataPreProcessingStrategy( DataStrategy):
    """
    Strategy for preprocessing data
    """
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        try:
            # data = data.d
            data = data.select_dtypes( include = [np.number])
            return data
        except Exception as e:
            logging.error("Error in preprocessing data: {}".format(e) )
            raise e

class DataDivideStrategy( DataStrategy):
    """
    Strategy for dividing into train and test
    """
    def handle_data(self, data: pd.DataFrame) -> Union[ pd.DataFrame , pd.Series]:
        try:
            X = data.drop( ["value"], axis=1) # time serie
            y = data["value"] # dolar value
            X_train, x_test, y_train, y_test = train_test_split( X, y , test_size=0.2, random_state=42)
            return X_train, x_test, y_train, y_test 
        except Exception as e:
            logging.error( "Error in dividing data: {e}".format(e))
            raise
        
class DataCleaning:
    """
    Class for cleaning data which processes the data and divides it into train and test
    """ 
    def __init__(self, data: pd.DataFrame, strategy: DataStrategy):
        self.data = data  
        self.strategy = strategy

    def handle_data(self) -> Union[ pd.DataFrame, pd.Series]:
        """
        Handle data
        """
        try:
            return self.strategy.handle_data( self.data)
        except Exception as e:
            logging.error( "Error in handling Data: {}".format(e) )
            raise e
        
if __name__ == "__main__":
    data = pd.read_csv("/workspaces/MLops-ZenML/data/olist_customers_dataset.csv")
    data_cleaning = DataCleaning(data, DataPreProcessStrategy)
    data_cleaning.handle_data()

