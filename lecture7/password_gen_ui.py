import tkinter
from password_gen import generate_password

def generate_button_called():
    new_password = generate_password()
    print("I'm here", new_password)
    password_label.config(text=f"Generated Password: {new_password}")

main_win = tkinter.Tk()
cv = tkinter.Canvas(width=300, height=300)
cv.grid(column=0, row=0, columnspan=1, rowspan=2)
generate_button = tkinter.Button(main_win, text="Generate Password", 
                                 command=generate_button_called)
generate_button.grid(row=0, column=0)

password_label = tkinter.Label(main_win, text="Generated Password:")
password_label.grid(row=1, column=0)
main_win.mainloop()