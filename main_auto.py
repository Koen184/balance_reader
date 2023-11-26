import tkinter as Tk
import app_auto


window = Tk.Tk()

App = app_auto.App(window)
app_auto.App.create_menu(App, window)

window.mainloop()
