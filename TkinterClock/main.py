from tkinter import *
from tkinter import ttk
from time import strftime

def Mainfunction():

    root = Tk()
    root.attributes("-fullscreen", True)

    background = Frame(root, background='white', width=1920, height=1080)
    background.place(x = 0, y = 0)

    def time():
        string = strftime("%H : %M")
        clockLabel.config(text = string, font = ('Gothic', 400), foreground = "black", background = "white")
        clockLabel.after(1000, time)

    clockLabel = ttk.Label(root)
    clockLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    exitButton = ttk.Button(root, text="X", command=exit, width= 5)
    exitButton.place(x=10, y=10)

    time()

    root.mainloop()

if __name__ == "__main__":
    Mainfunction()
