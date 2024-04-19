import logging
from abc import ABC, abstractclassmethod
from sklearn.linear_model import LinearRegression

import lightgbm as lgb
from lightgbm import LGBMRegressor


class Model(ABC):
    """
    Abstract  class for all models
    """
    @abstractclassmethod
    def train(self, X_train, y_train):
        """
        trains in model
        """
        pass

class LinearRegressionModel(Model):
    """
    trains the model
    """
    def  train(self, X_train, y_train, **kwargs):
        """
        Trains the model
        Args:
            X_train: training data
            y_train: training label
        Returns:
            None
        """
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info("Model training completed")
            return reg
        except Exception as e:
            logging.error("Error in cleaning data: {}".format(e))
            raise e

class LGBModel(Model):
    """
    trains the model
    """
    def  train(self, X_train, y_train, params):
        """
        Trains the model
        Args:
            X_train: training data
            y_train: training label
        Returns:
            None
        """
        try:
            train_data = lgb.Dataset(X_train, label=y_train)
            gbm = lgb.train(params, train_data, num_boost_round=200)

           # reg.fit(X_train, y_train)
            logging.info("Model training completed")
            return gbm
        except Exception as e:
            logging.error("Error in cleaning data: {}".format(e))
            raise e