import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ChartWindow:
    def __init__(self, wnd, data):
        self.wnd = wnd
        self.wnd.state('zoomed')
        self.data = data
        self.wnd.title('Графики')

        main_frame = tk.Frame(self.wnd)
        main_frame.pack(fill=tk.BOTH, expand=1)

        my_canvas = tk.Canvas(main_frame)

        v_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.FALSE)

        h_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=my_canvas.xview)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X, expand=tk.FALSE)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        my_canvas.configure(xscrollcommand=h_scroll.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        second_frame = tk.Frame(my_canvas)

        self.canvas = my_canvas

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.create_window((0, 0), window=second_frame, anchor="nw")

        self.frame = second_frame
        self.frame.focus_force()
        self.get_graph()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def get_graph(self):
        self.in_out_correlation_plot()
        self.in_out_structure_plot()
        # self.in_problem_structure_plot()
        # self.out_problem_structure_plot()
        # self.business_structure_plot()
        # self.business_type_structure_plot()
        # self.zgd_structure_plot()

    def zgd_structure_plot(self):
        plot_df = self.data.iloc[:,5].value_counts()
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.frame)
        bar1.get_tk_widget().grid()
        plot_df.plot(kind='pie', legend=True, ax=ax1)
        ax1.set_title('Распределение задач по ЗГД')

    def business_type_structure_plot(self):
        plot_df = self.data.iloc[:,4].value_counts()
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.frame)
        bar1.get_tk_widget().grid()
        plot_df.plot(kind='pie', legend=True, ax=ax1)
        ax1.set_title('Структура типов бизнесс процессов')

    def in_out_correlation_plot(self):
        plot_df = self.data.iloc[:,1].value_counts()
        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.frame)
        bar1.get_tk_widget().grid()
        plot_df.plot(kind='pie', legend=True, ax=ax1, wedgeprops=dict(width=0.5))
        ax1.set_title('Соотношение внешних и внутренних проблем')

    def in_out_structure_plot(self):
        plot_df = self.data.iloc[:,2].value_counts()
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        bar = FigureCanvasTkAgg(figure, self.frame)
        bar.get_tk_widget().grid(column=0, row=1)
        plot_df.plot(kind='pie', legend=True, ax=ax, wedgeprops=dict(width=0.5))
        ax.set_title('Структура внешних и внутренних проблем')

        plot_df1 = self.data.iloc[:,2].value_counts()
        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = figure1.add_subplot(111, projection="polar")
        bar1 = FigureCanvasTkAgg(figure1, self.frame)
        bar1.get_tk_widget().grid(column=1, row=1)
        plot_df1.plot(kind='pie', legend=True, ax=ax1, wedgeprops=dict(width=0.5))
        ax1.set_title('Структура внешних и внутренних проблем')

    def in_problem_structure_plot(self):
        mask = self.data.iloc[:, 1] == 'Внутренняя'
        plot_df1 = self.data[mask]
        df2 = plot_df1.iloc[:,2].value_counts()
        figure2 = plt.Figure(figsize=(6, 5), dpi=100)
        ax2 = figure2.add_subplot(111)
        bar2 = FigureCanvasTkAgg(figure2, self.frame)
        bar2.get_tk_widget().grid()
        df2.plot(kind='pie', legend=True, ax=ax2, wedgeprops=dict(width=0.5))
        ax2.set_title('Структура внутренних проблем')

    def out_problem_structure_plot(self):
        mask = self.data.iloc[:, 1] == 'Внешняя'
        plot_df1 = self.data[mask]
        df2 = plot_df1.iloc[:,2].value_counts()
        figure2 = plt.Figure(figsize=(6, 5), dpi=100)
        ax2 = figure2.add_subplot(111)
        bar2 = FigureCanvasTkAgg(figure2, self.frame)
        bar2.get_tk_widget().grid()
        df2.plot(kind='pie', legend=True, ax=ax2, wedgeprops=dict(width=0.5))
        ax2.set_title('Структура внешних проблем')

    def business_structure_plot(self):
        plot_df = self.data.iloc[:,3].value_counts()
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.frame)
        bar1.get_tk_widget().grid()
        plot_df.plot(kind='pie', legend=True, ax=ax1, wedgeprops=dict(width=0.5))
        ax1.set_title('Структура бизнесс процессов')