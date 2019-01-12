from tkinter import *
from tkinter import ttk

def open_window():
    #window = Toplevel()
    window = Tk()
    window.title("Save Some Text Buddy")
    window.geometry("600x600")

    mainWindowFrame = Frame(window)
    #mainwindowFrame.state("zoomed") #how to fill entire window frame?
    mainWindowFrame.pack(fill=BOTH, expand=1)

    #window's application menu
    menu = Menu(window)
    window.config(menu=menu)
    filemenu = Menu(menu)
    #Create different drop down file menus
    menu.add_cascade(label="File", menu=filemenu)
    menu.add_cascade(label="Options", menu=filemenu)
    #add the options for the dropdowns
    filemenu.add_command()


    #organization for the sections of this window
    topWindowFrame = Frame(mainWindowFrame)
    topWindowFrame.pack(fill=X, expand=1)
    middleWindowFrame = Frame(mainWindowFrame)
    middleWindowFrame.pack(fill=X, expand=1)
    bottomWindowFrame = Frame(mainWindowFrame)
    bottomWindowFrame.pack(fill=X, expand=1)

    #Section: topWindowFrame
    content = Text(topWindowFrame, height=20, width=50)
    content.pack(fill=X)
    content.insert(END, "Enter Some Text")

    #Section: middleWindowFrame
    label_path = Label(middleWindowFrame, text="File Path: ", padx=15,)
    label_path.grid(row=0, column=0)


    file_name = Entry(middleWindowFrame)
    file_name.grid(row=0, column=1)

    #Section: bottomWindowFrame
    #Holds all the options buttons
    submit_button = ttk.Button(bottomWindowFrame, text="Submit")
    submit_button.pack()
    clear_button = ttk.Button(bottomWindowFrame, text="Clear")
    clear_button.pack()
    exit_button = ttk.Button(bottomWindowFrame, text="Exit", command=window.destroy)
    exit_button.pack()

    window.mainloop()

open_window()
