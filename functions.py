# FUNCTIONS USED IN APP
import tkinter as Tk
import pandas as pd
import re


def window_size_position(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (screen_width / 4))
    y_coordinate = int((screen_height / 2) - (screen_height / 4))

    window.geometry("{}x{}+{}+{}".format(1200, 675, x_coordinate, y_coordinate))


def create_grid(window):
    Tk.Grid.rowconfigure(window, 0, weight=1)
    Tk.Grid.rowconfigure(window, 1, weight=1)
    Tk.Grid.rowconfigure(window, 2, weight=1)
    Tk.Grid.rowconfigure(window, 3, weight=1)
    Tk.Grid.rowconfigure(window, 4, weight=1)
    Tk.Grid.rowconfigure(window, 5, weight=1)
    Tk.Grid.rowconfigure(window, 6, weight=1)

    Tk.Grid.columnconfigure(window, 0, weight=1)
    Tk.Grid.columnconfigure(window, 1, weight=6)
    Tk.Grid.columnconfigure(window, 2, weight=6)


def save_to_excel(entry):
    with open('extraction_saved.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = []
    headers = ['Mine', '2018', '2019', '2020', '2021', '2022']
    for line in lines[1:]:
        pattern = r'^(.*?)\s(\d+|\-|N)\s(\d+|\-|N)\s(\d+|\-|N)\s(\d+|\-|N)\s(\d+|\-|N)\s*$'
        match = re.match(pattern, line.strip())
        if match:
            data.append(match.groups())

    excel = str(entry.get()) + '.xlsx'
    df = pd.DataFrame(data, columns=headers)
    df.to_excel(excel, index=False)


# Automatic balance reader

def window_size_position_auto(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (screen_width / 4))
    y_coordinate = int((screen_height / 2) - (screen_height / 4))

    window.geometry("{}x{}+{}+{}".format(660, 360, x_coordinate, y_coordinate))


def create_grid_auto(window):
    Tk.Grid.rowconfigure(window, 0, weight=1)
    Tk.Grid.rowconfigure(window, 1, weight=1)
    Tk.Grid.rowconfigure(window, 2, weight=1)

    Tk.Grid.columnconfigure(window, 0, weight=1)
    Tk.Grid.columnconfigure(window, 1, weight=6)


def save_to_excel_auto(entry):
    with open('extraction_saved_auto.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data_mine = []
    data_values = []
    headers = ['Mine', '2018', '2019', '2020', '2021', '2022']

    for line in lines[1:]:
        mine_match = re.search(r'^(.*?)\s(?:-|Not_found|\d)', line)
        if mine_match:
            mine = mine_match.group(1)
            values = re.sub(r'^' + re.escape(mine) + r'\s+', '', line.strip())
            data_mine.append(mine)
            data_values.append(values)

    # Splitting values by spaces and allocating them to respective columns
    data_values_split = [values.split() for values in data_values]
    data_values_columns = [[row[i] if len(row) > i else '' for row in data_values_split] for i in range(5)]

    # Creating a DataFrame
    data_dict = {'Mine': data_mine}
    for i, header in enumerate(headers[1:]):
        data_dict[header] = data_values_columns[i]

    excel = str(entry.get()) + '.xlsx'
    df = pd.DataFrame(data_dict)
    df.to_excel(excel, index=False)
