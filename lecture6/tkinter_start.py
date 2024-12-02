from tkinter import Tk
import tkinter
main_window = Tk()
main_window.title("THI-EGM SWD")

background_canvas = tkinter.Canvas(main_window, width=200, height=600)
background_canvas.grid(rowspan=4, columnspan=2)
label = tkinter.Label(main_window, text="Hello EGM")
label.grid(row=0, column=0)

button = tkinter.Button(main_window, text="Alright")
button.grid(row=3, column=0, columnspan=2)
#button.pack()
main_window.mainloop()