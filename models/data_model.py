from pysingleton import PySingleton
import pandas as pd

from services.parse_svg import SVGParser


class DataModel(metaclass=PySingleton):
    headers = [
        "Первичная формулировка",
        "Внешняя / Внутренняя",
        "Классификация проблеммы",
        "Бизнесс процесс",
        "Вид биснесс процесса",
        "З.Г.Д."
    ]


    def __init__(self):
        self.df = pd.DataFrame()
        self._create_empty_data()
        self.filename = 'new_file.csv'

    def _create_empty_data(self):
        problems = []
        column_num = len(self.headers)
        self.df = pd.DataFrame(problems, columns=[self.headers[0]])

    def load_from_csv(self, filename):
        self.filename = str.split(filename, '/')[-1]
        print(self.filename)
        self.df = pd.read_csv(filename)
        self.df = self.df.fillna(' ')

    def load_from_svg(self, filename):
        self.filename = str.split(filename, '/')[-1]
        problems = SVGParser.parse_svg(filename)
        column_num = len(self.headers)
        df = pd.DataFrame(problems, columns=[self.headers[0]])
        for i in range(1, column_num):
            df.insert(len(df.columns), self.headers[i], value='')
        self.df = df

