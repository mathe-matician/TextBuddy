from tkinter import *

root = Tk()
root.geometry("300x300")

def key(event):
    print("you pressed it: ", + repr(event.char))

def returnKey_pressed(event):
    g = repr(event.char)
    q = "\\r"
    if g == q:
        return validate_login()
    else:
        print("something went wrong")

def validate_login():
    print("You logged in!")

frame = Frame(root)

label = Label(frame, text="Entry 1").pack()
entry = Entry(frame)
entry.pack()

label2 = Label(frame, text="Entry 2").pack()
entry2 = Entry(frame)
entry2.pack()

entry.bind("<Return>", returnKey_pressed)
entry2.bind("<Return>", key)
frame.pack()

root.mainloop()
