from tkinter import Tk
import tkinter
main_window = Tk()
main_window.title("THI-EGM SWD")
label = tkinter.Label(main_window, text="Hello EGM")

button = tkinter.Button(main_window, text="Alright")
button.pack()
main_window.mainloop()