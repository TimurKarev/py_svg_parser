import tkinter as tk
from tkinter import filedialog

from models.data_model import DataModel


class StartWindow:
    def __init__(self, wnd):
        self.wnd = wnd
        self.wnd.title('Стартовое окно')

        button = tk.Button(self.wnd, text='Загрузить из SVG (Графика)', command=self._svg_load)
        button.grid()

        button = tk.Button(self.wnd, text='Загрузить из CSV (Таблица)', command=self._csv_load)
        button.grid(row=1)

        button = tk.Button(self.wnd, text='Создать с нуля', command=self._new_table)
        button.grid(row=2)

        self.wnd.attributes('-topmost', 'true')
        self.wnd.focus_force()
        self.wnd.mainloop()

    def _svg_load(self):
        print('svg_load')

    def _csv_load(self):
        self.wnd.attributes('-topmost', 'false')
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("csv files", "*.csv"),))
        model = DataModel()
        model.load_from_csv(filename)
        self.wnd.destroy()
        tk.Toplevel()
        print(model.df)

    def _new_table(self):
        print('new_table')