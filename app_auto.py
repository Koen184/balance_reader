import tkinter as Tk
import customtkinter as cTk
import  pandas as pd
import functions


class App:

    def __init__(self, window):
        window.title('Automatic balance reader')
        functions.window_size_position_auto(window)
        functions.create_grid_auto(window)

        self.county = ''
        self.path = ''
        self.mines = []
        self.results = []

    def create_menu(self, window):
        label_bg = Tk.Label(window, bg='#FFFFFF')
        label_bg.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="NSEW")

        entry_county = cTk.CTkEntry(window, placeholder_text="County", font=("Helvetica", 22, 'bold'), width=360,
                                    height=60, border_width=2, corner_radius=30, bg_color='#FFFFFF', fg_color='#FFFFFF',
                                    text_color='#000000')
        entry_county.grid(row=0, column=0)

        button_county = cTk.CTkButton(window, text='Read county', font=("Helvetica", 27, 'bold'), hover=True,
                                      hover_color='#000000', height=60, width=200, border_width=2, corner_radius=30,
                                      border_color='#FFFFFF', bg_color='#FFFFFF', fg_color="#262626",
                                      text_color='#FFFFFF', command=lambda: App.get_county(self, entry_county))
        button_county.grid(row=0, column=1)

        entry_path = cTk.CTkEntry(window, placeholder_text="Input path to excel file", font=("Helvetica", 22, 'bold'),
                                  width=360, height=60, border_width=2, corner_radius=30, bg_color='#FFFFFF',
                                  fg_color='#FFFFFF', text_color='#000000')
        entry_path.grid(row=1, column=0)

        entry_excel = cTk.CTkEntry(window, placeholder_text="Input new excel name", font=("Helvetica", 22, 'bold'),
                                   width=360, height=60, border_width=2, corner_radius=30, bg_color='#FFFFFF',
                                   fg_color='#FFFFFF', text_color='#000000')
        entry_excel.grid(row=2, column=0)

        button_path = cTk.CTkButton(window, text='Read mines', font=("Helvetica", 27, 'bold'), hover=True,
                                    hover_color='#000000', height=60, width=200, border_width=2, corner_radius=30,
                                    border_color='#FFFFFF', bg_color='#FFFFFF', fg_color="#262626",
                                    text_color='#FFFFFF', command=lambda: App.get_mines(self, entry_path))
        button_path.grid(row=1, column=1)

        def combined_function():
            App.save_to_txt(self)
            functions.save_to_excel_auto(entry_excel)

        button_excel = cTk.CTkButton(window, text='Save', font=("Helvetica", 27, 'bold'), hover=True,
                                     hover_color='#000000', height=60, width=200, border_width=2, corner_radius=30,
                                     border_color='#FFFFFF', bg_color='#FFFFFF', fg_color="#262626",
                                     text_color='#FFFFFF', command=lambda: combined_function())
        button_excel.grid(row=2, column=1)

    def get_county(self, entry):
        self.county = str(entry.get())

    def get_mines(self, entry):
        self.path = str(entry.get())
        self.path = self.path[1:-1]

        excel = pd.read_excel(self.path, index_col=0)
        self.mines = (excel.iloc[:, 2]).tolist()

        for mine in self.mines:

            result_mine = []

            for year in range(2018, 2023):
                filename = f"balance_{year}.txt"
                filepath = f"balances/{filename}"

                with open(filepath, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                    found_value = False
                    for line in lines:
                        if mine in line and self.county in line:
                            parts = line.split(self.county)
                            value = parts[0].split()[-1]

                            if len(value) == 3 and len(parts[0].split()[-2]) < 3:
                                value = parts[0].split()[-2] + value

                            result_mine.append(value.strip())
                            found_value = True
                            break

                    if not found_value:
                        for i in range(len(lines) - 1):
                            line = lines[i].strip()
                            next_line = lines[i + 1].strip()

                            if mine in line and self.county in next_line:
                                parts = next_line.split(self.county)
                                value = parts[0].split()[-1]

                                if len(value) == 3 and len(parts[0].split()[-2]) < 3:
                                    value = parts[0].split()[-2] + value

                                result_mine.append(value.strip())
                                found_value = True
                                break

                        if not found_value:
                            result_mine.append("Not_found")

            self.results.append(result_mine)

    def save_to_txt(self):
        text_file = 'extraction_saved_auto.txt'

        with open(text_file, 'a', encoding='utf-8') as file:
            headers = 'Mine 2018 2019 2020 2021 2022\n'
            file.write(headers)

            for i in range(len(self.mines)):
                mine_data = self.results[i]
                data = f"{self.mines[i]} {' '.join(map(str, mine_data))}\n"
                file.write(data)


