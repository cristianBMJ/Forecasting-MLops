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
            data = data.drop(["Codigo", "Nombre", "Fecha"], axis=1)
            data['Valor'] = pd.to_numeric(data['Valor'].str.replace(',', '.'))
            #data["Fecha"] = pd.to_datetime( data["Fecha"]) 
            data["time"] = data.index 
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
            X = data.drop( ["Valor"], axis=1) # time serie
            y = data["Valor"] # dolar value
            X_train, x_test, y_train, y_test = train_test_split( X, y , test_size=0.2, random_state=42)
            return X_train, x_test, y_train, y_test 
        except Exception as e:
            logging.error( "Error in dividing data: {}".format(e))
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
    data_path = "/workspaces/Forecasting-MLops/data/extracted_data.json"
    data = pd.read_json(data_path)
    data_cleaning = DataCleaning(data, DataPreProcessStrategy)
    data_cleaning.handle_data()

