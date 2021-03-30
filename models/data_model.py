from pysingleton import PySingleton
import pandas as pd


class DataModel(metaclass=PySingleton):
    def __init__(self):
        self.df = pd.DataFrame()

    def load_from_csv(self, filename):
        self.df = pd.read_csv(filename)
        self.df.fillna(' ')
