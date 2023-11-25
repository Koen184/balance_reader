import tkinter as Tk
import customtkinter as cTk
import functions


class App:

    def __init__(self, window):
        window.title('Balance reader')
        functions.window_size_position(window)
        functions.create_grid(window)

        self.county = ''
        self.mine = ''
        self.results = []
        self.entry_list = []
        self.index = 1

    def create_side_panel(self, window):
        label_bg = Tk.Label(window, bg='#FF69B4')
        label_bg.grid(row=0, column=0, rowspan=7, sticky="NSEW")

        label1 = Tk.Label(window, text="BALANCE READER", font=("Helvetica", 36, 'bold'), fg='#FFFFFF', bg='#FF69B4')
        label1.grid(row=0, column=0)

        entry_county = cTk.CTkEntry(window, placeholder_text="County", font=("Helvetica", 22, 'bold'), width=300,
                                    height=60, border_width=2, corner_radius=30, bg_color='#FF69B4', fg_color='#FFFFFF',
                                    text_color='#000000')
        entry_county.grid(row=1, column=0)

        button_county = cTk.CTkButton(window, text='Read county', font=("Helvetica", 27, 'bold'), hover=True,
                                      hover_color='#000000', height=60, width=200, border_width=2, corner_radius=30,
                                      border_color='#FFFFFF', bg_color='#FF69B4', fg_color="#262626",
                                      text_color='#FFFFFF', command=lambda: App.get_county(self, entry_county))
        button_county.grid(row=2, column=0)

        entry_mine = cTk.CTkEntry(window, placeholder_text="Mine", font=("Helvetica", 22, 'bold'), width=300,
                                  height=60, border_width=2, corner_radius=30, bg_color='#FF69B4', fg_color='#FFFFFF',
                                  text_color='#000000')
        entry_mine.grid(row=3, column=0)

        def combined_function():
            App.get_mine(self, entry_mine)
            App.extraction_into_entries(self)

        button_mine = cTk.CTkButton(window, text='Read mine', font=("Helvetica", 27, 'bold'), hover=True,
                                    hover_color='#000000', height=60, width=200, border_width=2, corner_radius=30,
                                    border_color='#FFFFFF', bg_color='#FF69B4', fg_color="#262626",
                                    text_color='#FFFFFF', command=lambda: combined_function())
        button_mine.grid(row=4, column=0)

        entry_excel = cTk.CTkEntry(window, placeholder_text="Excel name", font=("Helvetica", 22, 'bold'), width=300,
                                   height=60, border_width=2, corner_radius=30, bg_color='#FF69B4', fg_color='#FFFFFF',
                                   text_color='#000000')
        entry_excel.grid(row=5, column=0)

        button_excel = cTk.CTkButton(window, text='Create excel', font=("Helvetica", 27, 'bold'), hover=True,
                                     hover_color='#000000', height=60, width=200, border_width=2, corner_radius=30,
                                     border_color='#FFFFFF', bg_color='#FF69B4', fg_color="#262626",
                                     text_color='#FFFFFF', command=lambda: functions.save_to_excel(entry_excel))
        button_excel.grid(row=6, column=0)

    def create_menu(self, window):
        label_bg = Tk.Label(window, bg='#FFFFFF')
        label_bg.grid(row=0, column=1, rowspan=7, columnspan=2, sticky="NSEW")

        label_title1 = Tk.Label(window, text="BALANCE YEAR", font=("Helvetica", 26, 'bold'), fg='#353935', bg='#FFFFFF')
        label_title1.grid(row=0, column=1)

        years = ['2018', '2019', '2020', '2021', '2022']

        for i, year in enumerate(years):
            label_year = Tk.Label(window, text=year, font=("Helvetica", 26, 'bold'), fg='#353935', bg='#FFFFFF')
            label_year.grid(row=(i + 1), column=1)

        label_title2 = Tk.Label(window, text="EXTRACTION", font=("Helvetica", 26, 'bold'), fg='#353935', bg='#FFFFFF')
        label_title2.grid(row=0, column=2)

        entry_extraction2018 = cTk.CTkEntry(window, placeholder_text="Extraction 2018", font=("Helvetica", 22, 'bold'),
                                            width=300, height=60, border_width=2, corner_radius=30, bg_color='#FFFFFF',
                                            fg_color='#FFFFFF', text_color='#000000')

        entry_extraction2019 = cTk.CTkEntry(window, placeholder_text="Extraction 2019", font=("Helvetica", 22, 'bold'),
                                            width=300, height=60, border_width=2, corner_radius=30, bg_color='#FFFFFF',
                                            fg_color='#FFFFFF', text_color='#000000')

        entry_extraction2020 = cTk.CTkEntry(window, placeholder_text="Extraction 2020", font=("Helvetica", 22, 'bold'),
                                            width=300, height=60, border_width=2, corner_radius=30, bg_color='#FFFFFF',
                                            fg_color='#FFFFFF', text_color='#000000')

        entry_extraction2021 = cTk.CTkEntry(window, placeholder_text="Extraction 2021", font=("Helvetica", 22, 'bold'),
                                            width=300, height=60, border_width=2, corner_radius=30, bg_color='#FFFFFF',
                                            fg_color='#FFFFFF', text_color='#000000')

        entry_extraction2022 = cTk.CTkEntry(window, placeholder_text="Extraction 2022", font=("Helvetica", 22, 'bold'),
                                            width=300, height=60, border_width=2, corner_radius=30, bg_color='#FFFFFF',
                                            fg_color='#FFFFFF', text_color='#000000')

        self.entry_list = [entry_extraction2018, entry_extraction2019, entry_extraction2020,
                           entry_extraction2021, entry_extraction2022]

        for i, entry in enumerate(self.entry_list):
            entry.grid(row=(i + 1), column=2)

        button_saveto_excel = cTk.CTkButton(window, text='Save to text file', font=("Helvetica", 27, 'bold'),
                                            hover=True,
                                            hover_color='#000000', height=60, width=200, border_width=2,
                                            corner_radius=30, border_color='#FFFFFF', bg_color='#FFFFFF',
                                            fg_color="#262626", text_color='#FFFFFF', command=lambda:
            App.save_to_txt(self))
        button_saveto_excel.grid(row=6, column=2)

    def get_county(self, entry):
        self.county = str(entry.get())

    def get_mine(self, entry):
        self.mine = str(entry.get())

        self.results = []

        for year in range(2018, 2023):
            filename = f"balance_{year}.txt"
            filepath = f"balances/{filename}"

            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                found_value = False
                for line in lines:
                    if self.mine in line and self.county in line:
                        parts = line.split(self.county)
                        value = parts[0].split()[-1]

                        if len(value) == 3 and len(parts[0].split()[-2]) < 3:
                            value = parts[0].split()[-2] + value

                        self.results.append(value.strip())
                        found_value = True
                        break

                if not found_value:
                    for i in range(len(lines) - 1):
                        line = lines[i].strip()
                        next_line = lines[i + 1].strip()

                        if self.mine in line and self.county in next_line:
                            parts = next_line.split(self.county)
                            value = parts[0].split()[-1]

                            if len(value) == 3 and len(parts[0].split()[-2]) < 3:
                                value = parts[0].split()[-2] + value

                            self.results.append(value.strip())
                            found_value = True
                            break

                    if not found_value:
                        self.results.append("Not found")

    def extraction_into_entries(self):
        for i, entry in enumerate(self.entry_list):
            entry.delete(0, Tk.END)
            entry.insert(0, self.results[i])

    def save_to_txt(self):
        transposed_results = [list(row) for row in zip(*self.results)]

        text_file = 'extraction_saved.txt'

        with open(text_file, 'a', encoding='utf-8') as file:
            if self.index == 1:
                headers = 'Mine 2018 2019 2020 2021 2022\n'
                file.write(headers)

            data = f"{self.mine} {' '.join(map(str, transposed_results[0]))}\n"
            file.write(data)

        self.index += 1
