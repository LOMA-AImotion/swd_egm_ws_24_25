import tkinter
import tkinter.messagebox

def say_hi():
    print("Hi EGM")
    tkinter.messagebox.showwarning("THI-EGM", "Hi, how are you?")
    button.config(text="Servus!")

main_win = tkinter.Tk()
button = tkinter.Button(main_win, text="Say Hi!", command=say_hi)
button.pack()
main_win.mainloop()