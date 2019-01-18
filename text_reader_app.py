from tkinter import *
from tkinter import ttk, messagebox
import json
from properties import config

def open_window():
    #-------------------------------------------------------------
    #Create root window and establish bells and whistles
    #Create frame (mainWindowFrame) for root window for management
    #-------------------------------------------------------------
    #window = Toplevel()
    window = Tk()
    window.title(config["WINDOW_TITLE"])
    window.geometry(config["WINDOW_GEOMETRY"])
    window.iconbitmap(config["WINDOW_ICONBITMAP"])

    mainWindowFrame = Frame(window)
    mainWindowFrame.pack(fill=BOTH, expand=0)

    #-------------------------------------------------------------
    #window's application menu
    #-------------------------------------------------------------
    menubar = Menu(window)
    #Create File menu dropdown with commmands inside
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label=config["WINDOW_FILE_DROPDOWN_MENU"], menu=filemenu)
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

    notebook.pack(fill=X, expand=0)

    ##############################################################
    #########################  Tab 1  ############################
    ##############################################################
    #create frames for management
    topWindowFrame = Frame(tab1)
    topWindowFrame.pack(fill=X, expand=0)
    middleWindowFrame = Frame(mainWindowFrame)
    middleWindowFrame.pack(fill=X, expand=0)
    bottomWindowFrame = Frame(mainWindowFrame)
    bottomWindowFrame.pack(fill=X, expand=0)

    #-------------------------------------------------------------
    #Section: topWindowFrame
    #Main textbox
    #-------------------------------------------------------------
    def unbind_return_and_key(event):
        content.delete("1.0", END)
        content.unbind("<Button-1>")
        content.unbind("<Key>")
        content.config(state=NORMAL)

    panda_image = PhotoImage(file="C:\\Users\\Zach\\Documents\\Git\\textprogram\\graphics\\redpanda_trans.gif")
    content = Text(topWindowFrame, height=20, width=50)
    content.pack(fill=X, expand=0)
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
        content.bind("<Button-1>", unbind_return_and_key)

    def save_to_my_notes():
        tab_one_content = content.get("1.0", END)
        content.delete("1.0", END)
        tab2_textbox.insert("1.0", tab_one_content)

    def save_to_text_file():
        text_content = content.get("1.0", END)
        data = {"Data Fun Time": text_content}
        name = "testfile"
        with open("obj/" + "data.txt", "w") as file:
            json.dump(data, file)
        content.delete("1.0", END)

    def quit_program():
        if messagebox.askokcancel("Quit Program?", "You have unsaved work, are you sure you want to quit?"):
            return window.destroy()

    submit_button = ttk.Button(bottomWindowFrame, text="Save to My Notes", padding=6, command=save_to_my_notes)
    submit_button.grid(row=0, column=0)
    save_to_file = ttk.Button(bottomWindowFrame, text="Save to Text File", padding=6, command=save_to_text_file)
    save_to_file.grid(row=0, column=1)
    clear_button = ttk.Button(bottomWindowFrame, text="Clear All", padding=6, command=clear_all_fields)
    clear_button.grid(row=0, column=2)
    exit_button = ttk.Button(bottomWindowFrame, text="Exit", padding=6, command=quit_program)
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
    my_notes_main_frame = ttk.Frame(tab2, height=15, width=100)
    my_notes_main_frame.pack(expand=0)
    note_list_frame = ttk.Frame(my_notes_main_frame, height=10, width=160)
    #note_list_frame.grid_propagate(False)
    note_list_frame.pack(side=LEFT, expand=0)
    note_display_frame = ttk.Frame(my_notes_main_frame)
    note_display_frame.grid_propagate(False)
    note_display_frame.pack(padx=10, expand=0)

    #-------------------------------------------------------------
    #Create the notebook to load multiple notes
    #-------------------------------------------------------------
    def close_tab():
        display_textbox.pack_forget()


    my_notes_notebook = ttk.Notebook(note_display_frame)
    my_notes_tab = ttk.Frame(my_notes_notebook)

    my_notes_notebook.add(my_notes_tab, text="Test")
    my_notes_notebook.pack()

    display_textbox = Text(my_notes_tab, height=19.3, width=50, state=DISABLED)
    display_textbox.pack()

    def create_new_tab(note_name):
        temporary_tab = ttk.Frame(my_notes_notebook)
        my_notes_notebook.add(temporary_tab, text=note_name)


    def load_text_from_file(note_name): #move this function into a new module once finished
        with open("obj/" + note_name + ".txt") as file:
            data = json.load(file)
            display_textbox.config(state=NORMAL)
            #if all tabs have been closed create a new textbox to display data
            #if display_textbox == display_textbox.pack_forget():
                #display_textbox = Text(my_notes_tab, height=19.3, width=50, state=DISABLED)
                #display_textbox.pack()
            display_textbox.delete("1.0", END)
            for k, v in dict.items(data):
                display_textbox.insert(INSERT, k + ":\n" + v)

    #make the scrollbar for box of notes & listbox for links
    scrollbar = Scrollbar(note_list_frame)
    scrollbar.pack(side=RIGHT, fill=Y, expand=0)
    note_box = Listbox(note_list_frame, yscrollcommand=scrollbar.set, width=20, height=11)
    note_box.bind("<Double-Button-1>", load_text_from_file)

    list_of_notes = ["note1", "note2", "note3", "note4"]
    for item in list_of_notes:
        note_box.insert(END, item)

    #for item in range(50):
        #note_box.insert(END, "This is: " + str(item))

    note_box.pack(side=TOP, fill=BOTH)
    scrollbar.config(command=note_box.yview)

    #Buttons in note list frame
    load_selected_file = Button(note_list_frame, text="Load Selected Note", command=load_text_from_file)
    load_selected_file.pack(side=TOP)
    delete_note_button = Button(note_list_frame, text="Delete Selected Note",
                                command= lambda note_box=note_box: note_box.delete(ANCHOR))
    delete_note_button.pack()
    closeTab = Button(note_list_frame, text="Close Current Tab", command=close_tab)
    closeTab.pack(side=TOP)

    file_button = ttk.Button(note_list_frame, text="File's Name Eventually", padding=17, command=load_text_from_file)
    #note_box.insert(END, file_button)
    #file_button.pack()

    close_tab_button = ttk.Button(note_list_frame, text="Close Tab", padding=17, command=close_tab)
    #note_box.insert(END, close_tab_button)
    #close_tab_button.pack()


    window.mainloop()

open_window()
