from tkinter import *
from tkinter import messagebox

window= Tk()
window.title("Event Handler")
window.geometry("300x300")

def handle_keypress(event):
    #print the character associted to the key pressed
    print(event.char)

window.bind("<Key>", handle_keypress)

button = Button(window, text="Click Me!")
button.pack()

def handle_click(event):
    messagebox.showinfo("Click Event", "You Clicked Me!")

button.bind("<Button-1>", handle_click)

def msg():
    messagebox.showerror("Alert!", "STOP! Virus Found!")

button2 = Button(window, text="Scan for virus!", command=msg)
button2.pack(pady=8)







window.mainloop()
