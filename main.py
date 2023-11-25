import tkinter as Tk
import app


window = Tk.Tk()

App = app.App(window)
app.App.create_side_panel(App, window)
app.App.create_menu(App, window)

window.mainloop()
