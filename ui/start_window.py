import tkinter as tk
from tkinter import filedialog

from models.data_model import DataModel


class StartWindow:
    def __init__(self, wnd, updateParent):
        self.wnd = wnd
        self.wnd.title('Стартовое окно')

        self.updateParent = updateParent

        button = tk.Button(self.wnd, text='Загрузить из SVG (Графика)', command=self._svg_load,
                           height='5', width='40')
        button.grid(padx='50', pady='20')

        button = tk.Button(self.wnd, text='Загрузить из CSV (Таблица)', command=self._csv_load,
                           height='5', width='40')
        button.grid(row=1, padx='50', pady='20')

        button = tk.Button(self.wnd, text='Создать с нуля', command=self._new_table,
                           height='5', width='40')
        button.grid(row=2, padx='50', pady='20')

        self.wnd.attributes('-topmost', 'true')
        self.wnd.focus_force()
        self.wnd.mainloop()

    def _svg_load(self):
        self.wnd.attributes('-topmost', 'false')
        filename = filedialog.askopenfilename(initialdir="C:/Users/User/Documents/Project/py_svg_parser", title="Select file",
                                              filetypes=(("svg files", "*.svg"),))
        model = DataModel()
        model.load_from_svg(filename)
        self.updateParent()
        self.wnd.destroy()

    def _csv_load(self):
        self.wnd.attributes('-topmost', 'false')
        filename = filedialog.askopenfilename(initialdir="C:/Users/User/Documents/Project/py_svg_parser", title="Select file",
                                              filetypes=(("csv files", "*.csv"),))
        model = DataModel()
        model.load_from_csv(filename)
        self.updateParent()
        self.wnd.destroy()

    def _new_table(self):
        filename = filedialog.asksaveasfilename(initialdir="C:/Users/User/Documents/Project/py_svg_parser",
                                              title="Select file",
                                              filetypes=(("svg files", "*.csv"),))
        model = DataModel()
        model.new_table(filename)
        self.updateParent()
        self.wnd.destroy()