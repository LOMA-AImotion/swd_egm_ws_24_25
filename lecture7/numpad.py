# Create a numpad with buttons for numbers 
# from 1 to 9 arranged in a 3x3 grid

from tkinter import Tk
import tkinter
main_window = Tk()
bg_canvas = tkinter.Canvas(main_window, width=400, height=400)
bg_canvas.grid(columnspan=3, rowspan=3)

i = 1
for row in range(0, 3):
    for col in range(0, 3):
        next_button = tkinter.Button(text=str(i), width=10, height=10)
        next_button.config(height=5)
        next_button.grid(row=row, column=col)
        i += 1

    
main_window.mainloop()