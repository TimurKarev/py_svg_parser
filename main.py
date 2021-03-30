from tkinter import *
from tkinter import filedialog
import pandas as pd
from services.parse_svg import SVGParser
from ui.chart_window import ChartWindow

headers = [
    "Первичная формулировка",
    "Внешняя / Внутренняя",
    "Классификация проблеммы",
    "Бизнесс процесс",
    "Вид биснесс процесса",
    "З.Г.Д."
]

drop_opt_1 = [
    "Внешняя",
    "Внутренняя"
]


def goto_charts():
    global df
    update_dataframe()
    save_df()
    new_window = Toplevel(root)
    ChartWindow(new_window, df)


def save_df():
    update_dataframe()
    global df
    df.to_csv('current_test.csv', index=False, encoding='utf-8-sig')


def clear_grid():
    global df
    for widget in root.grid_slaves():
        widget.grid_forget()
    root.deiconify()


def add_row():
    global df
    update_dataframe()
    d = {}
    for i in range(len(df.columns)):
        d[df.columns[i]] = ' '
    df = df.append(d, ignore_index=True)
    updateTable()


def delRow(row_num):
    global df
    update_dataframe()
    df.drop([df.index[row_num]], inplace=True)
    updateTable()

def update_dataframe():
    global df
    global ar
    for c in range(len(df.columns)):
        for r in range(df.shape[0]):
            df.iloc[r,c] = ar[r][c].get().strip()
    updateTable()

def updateTable():
    global ar
    global df
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
                edit = Entry(root, textvariable=txt, width='75')
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

    button = Button(root, text='   V   ', command=save_df)
    button.grid(column=len(df.columns)-1, columnspan=2, row=df.shape[0] + 1)

    button = Button(root, text='       ->        ', command=goto_charts)
    button.grid(column=len(df.columns), columnspan=3, row=df.shape[0] + 1)

if __name__ == '__main__':
    root = Tk()
    df = pd.DataFrame()
    ar = []

    try:
        root.filename = filedialog.askopenfilename()  # (initialdir="/", title="Select file",
        # filetypes=(("svg files", "*.svg"), ("all files", "*.*")))
    except:
        print('kda;ldska;ldk;')

    if root.filename[-3:] == 'svg':
        problems = SVGParser.parse_svg(root.filename)
        column_num = len(headers)
        df = pd.DataFrame(problems, columns=[headers[0]])
        for i in range(1, column_num):
            df.insert(len(df.columns), headers[i], value='')
    elif root.filename[-3:] == 'csv':
        df = pd.read_csv('current_test.csv')
        df = df.fillna(' ')

    updateTable()

    root.focus_force()
    root.mainloop()
