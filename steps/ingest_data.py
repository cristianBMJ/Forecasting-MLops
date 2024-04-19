import logging

import pandas as pd
from zenml import step

class IngestData:
    """
    Ingesting the data from the data_path
    """
    def __init__(self, data_path: str):
        """
        Args:
        data_path: path to the data
        """
        self.data_path = data_path

    def get_data(self) -> pd.DataFrame:
        logging.info(f"Ingesting data from {self.data_path}")  
        if self.data_path.endswith('.csv'):
            return pd.read_csv(self.data_path)
        elif self.data_path.endswith('.json'):
            return pd.read_json(self.data_path)
        else:
            raise ValueError("Unsupported file format. Only CSV and JSON files are supported.")

@step 
def ingest_df(data_path: str) -> pd.DataFrame:
    """
    Ingesting data from the data_path

    Args: 
        data_path: path to the data
    
    Return:
        pd.DataFrame: the ingested data
    """

    try:
        ingest_data = IngestData(data_path) # aplied class IngestData
        df = ingest_data.get_data() # from the path, is local. Here ingest might change its origin
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")