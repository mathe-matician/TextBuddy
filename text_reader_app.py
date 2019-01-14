from tkinter import *
from tkinter import ttk, messagebox
import json

def open_window():

    #-------------------------------------------------------------
    #Create root window and establish bells and whistles
    #Create frame (mainWindowFrame) for root window for management
    #-------------------------------------------------------------
    #window = Toplevel()
    window = Tk()
    window.title("Text Buddy")
    window.geometry("600x500")
    window.iconbitmap(r"C:\\Users\\Zach\\Documents\\Git\\textprogram\\favicon\\favicon.ico")

    mainWindowFrame = Frame(window)
    mainWindowFrame.pack(fill=BOTH, expand=1)

    #-------------------------------------------------------------
    #window's application menu
    #-------------------------------------------------------------
    menubar = Menu(window)
    #Create File menu dropdown with commmands inside
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Quit", command=window.quit)
    #Create Option menu dropdown with commands inside
    optionsmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=optionsmenu)
    optionsmenu.add_command(label="Don't look in here", command=NONE)
    #Create Help menu dropdown with commands inside
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)

    def about_alert():
        return messagebox.showinfo("Text Buddy v0.1", "Red pandas are kind of cool")

    helpmenu.add_command(label="About", command=about_alert)
    #display the menu
    window.config(menu=menubar)

    #-------------------------------------------------------------
    #Create notebook & frames for the tabs
    #-------------------------------------------------------------

    notebook = ttk.Notebook(mainWindowFrame)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)

    notebook.add(tab1, text="Write")
    notebook.add(tab2, text="My Notes")

    notebook.pack(fill=X)

    ##############################################################
    #########################  Tab 1  ############################
    ##############################################################
    #create frames for management
    topWindowFrame = Frame(tab1)
    topWindowFrame.pack(fill=X)
    middleWindowFrame = Frame(mainWindowFrame)
    middleWindowFrame.pack(fill=X)
    bottomWindowFrame = Frame(mainWindowFrame)
    bottomWindowFrame.pack(fill=X)

    #-------------------------------------------------------------
    #Section: topWindowFrame
    #Main textbox
    #-------------------------------------------------------------
    def unbind_return_and_key(event):
        content.delete("1.0", END)
        content.unbind("<Button-1>")
        content.unbind("<Key>")

    panda_image = PhotoImage(file="C:\\Users\\Zach\\Documents\\Git\\textprogram\\graphics\\redpanda_trans.gif")
    content = Text(topWindowFrame, height=20, width=50)
    content.pack(fill=X)
    content.image_create(END, image=panda_image, padx=160, pady=40)
    content.bind("<Button-1>", unbind_return_and_key)
    content.bind("<Key>", unbind_return_and_key)

    #-------------------------------------------------------------
    #Section: middleWindowFrame
    #-------------------------------------------------------------
    label_path = Label(middleWindowFrame, text="File Path: ", font="Calibri", padx=10, pady=20)
    label_path.grid(row=0, column=0)

    file_name = Entry(middleWindowFrame)
    file_name.grid(row=0, column=1)

    #-------------------------------------------------------------
    #Section: bottomWindowFrame
    #Holds all the options buttons
    #-------------------------------------------------------------
    def clear_all_fields():
        file_name.delete(0, END)
        content.delete("1.0", END)
        content.image_create(END, image=panda_image, padx=160, pady=40)
        content.bind("<Button-1>", unbind_return_key)

    def save_to_my_notes():
        tab_one_content = content.get("1.0", END)
        content.delete("1.0", END)
        tab2_textbox.insert("1.0", tab_one_content)

    def save_to_text_file():
        text_content = content.get("1.0", END)
        data = {"My Bob": text_content}
        name = "testfile"
        with open("obj/" + "data.txt", "w") as file:
            json.dump(data, file)
        content.delete("1.0", END)

    submit_button = ttk.Button(bottomWindowFrame, text="Save to My Notes", padding=6, command=save_to_my_notes)
    submit_button.grid(row=0, column=0)
    save_to_file = ttk.Button(bottomWindowFrame, text="Save to Text File", padding=6, command=save_to_text_file)
    save_to_file.grid(row=0, column=1)
    clear_button = ttk.Button(bottomWindowFrame, text="Clear All", padding=6, command=clear_all_fields)
    clear_button.grid(row=0, column=2)
    exit_button = ttk.Button(bottomWindowFrame, text="Exit", padding=6, command=window.destroy)
    exit_button.grid(row=0, column=3)

    ##############################################################
    #########################  Tab 2  ############################
    ##############################################################

    #-------------------------------------------------------------
    #create frames for management
    #main frame for tab2
    #frames to split tab 2 into two sections one scrollbox to hold
    #any create files & one to load the files into to edit
    #-------------------------------------------------------------
    my_notes_main_frame = ttk.Frame(tab2)
    my_notes_main_frame.pack()
    note_list_frame = ttk.Frame(my_notes_main_frame, height=70, width=160)
    note_list_frame.grid_propagate(False)
    note_list_frame.pack(side=LEFT)
    note_display_frame = ttk.Frame(my_notes_main_frame)
    note_display_frame.grid_propagate(False)
    note_display_frame.pack(padx=10)

    #-------------------------------------------------------------
    #Create the notebook to load multiple notes
    #-------------------------------------------------------------

    my_notes_notebook = ttk.Notebook(note_display_frame)
    my_notes_tab = ttk.Frame(my_notes_notebook)

    my_notes_notebook.add(my_notes_tab, text="Test")
    my_notes_notebook.pack()

    #testlabel = Label(my_notes_tab, text="A Label")
    #testlabel.pack()

    display_textbox = Text(my_notes_tab, height=19.3, width=50)
    display_textbox.pack()

    def load_text_from_file(): #move this function into a new module once finished
        with open("obj/" + "data.txt") as file:
            data = json.load(file)
            display_textbox.delete("1.0", END)
            for k, v in dict.items(data):
                display_textbox.insert(INSERT, k + ":\n" + v)

    file_button = ttk.Button(note_list_frame, text="File's Name Eventually", padding=17, command=load_text_from_file)
    file_button.grid(row=0, column=0)


    window.mainloop()

open_window()
