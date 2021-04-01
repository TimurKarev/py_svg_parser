from tkinter import *
from tkinter import filedialog
from pathlib import Path
import pandas as pd

from models.data_model import DataModel
from services.parse_svg import SVGParser
from ui.chart_window import ChartWindow
from ui.start_window import StartWindow

drop_opt_1 = [
    "Внешняя",
    "Внутренняя"
]


ar = []

def goto_charts():
    df = DataModel().df
    update_dataframe()
    save_df()
    new_window = Toplevel(root)
    ChartWindow(new_window, df)


def save_df():
    df = DataModel().df
    df.to_csv(DataModel().filename, index=False, encoding='utf-8-sig')

def save_as_df():
    filename = filedialog.asksaveasfilename(initialdir=Path().cwd(),
                                            title="Select file",
                                            filetypes=(("csv files", "*.csv"),))
    if filename[-4:] != '.csv':
        filename = filename + '.csv'
    DataModel().filename = Path(filename)
    save_df()

def clear_grid():
    for widget in root.grid_slaves():
        widget.grid_forget()
    root.deiconify()


def add_row():
    df = DataModel().df
    d = {}
    for i in range(len(df.columns)):
        d[df.columns[i]] = ' '
    DataModel().df = df.append(d, ignore_index=True)
    updateTable()



def delRow(row_num):
    df = DataModel().df
    df.drop([df.index[row_num]], inplace=True)
    updateTable()


def update_dataframe():
    df = DataModel().df
    global ar
    for c in range(len(df.columns)):
        for r in range(df.shape[0]):
            df.iloc[r, c] = ar[r][c].get().strip()
    updateTable()


def updateTable():
    global ar
    global root

    df = DataModel().df
    clear_grid()
    m = len(df.columns)
    ar = [[0] * m for i in range(df.shape[0])]
    for i, c in enumerate(df.columns):
        Label(text=c).grid(column=i + 1, row=0)

    for c in range(len(df.columns) + 1):
        for r in range(1, df.shape[0] + 1):
            if c == 0:
                button = Button(root, text='-', command=lambda row=r - 1: delRow(row))
                button.grid(column=c, row=r)
            elif c == 1:
                txt = StringVar(root, df.iloc[r - 1, 0])
                ar[r-1][c-1] = txt
                edit = Entry(root, textvariable=txt, width='100')
                edit.focus()
                edit.grid(column=c, row=r)
            elif c == 2:
                variable = StringVar(root)
                ar[r - 1][c-1] = variable
                variable.set(df.iloc[r - 1, c-1])  # default value
                w = OptionMenu(root, variable, *drop_opt_1)
                w.grid(column=c, row=r)
            else:
                txt = StringVar(root, df.iloc[r - 1, c-1])
                ar[r-1][c-1] = txt
                edit = Entry(root, textvariable=txt)
                edit.focus()
                edit.grid(column=c, row=r)

    button = Button(root, text='+', command=add_row)
    button.grid(column=0, row=df.shape[0] + 1)

    button = Button(root, text='   V   ', command=save_as_df)
    button.grid(column=len(df.columns)-1, columnspan=2, row=df.shape[0] + 1)

    button = Button(root, text='       ->        ', command=goto_charts)
    button.grid(column=len(df.columns), columnspan=3, row=df.shape[0] + 1)

    root.title(DataModel().filename)


if __name__ == '__main__':
    root = Tk()
    root.title('Main Window')
    start_window = Toplevel(root)
    StartWindow(start_window, updateTable)