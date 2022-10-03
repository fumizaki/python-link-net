# python standard library
from abc import ABC, abstractmethod
# python external library
import pandas as pd


class AbsMaster(ABC):

    @abstractmethod
    def set():
        raise NotImplementedError


    @abstractmethod
    def load():
        raise NotImplementedError


    @staticmethod
    def sorted_by(df: pd.DataFrame, column, asc=True):
        return df.sort_values(by=column, ascending=asc)