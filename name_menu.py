from tkinter import *
from tkinter import ttk
from text_reader_app import open_window
import time
#import run

class App:

    def __init__(self, master, *args):
        self.frame1 = ttk.Frame(master)
        self.frame1.pack()

        self.entry_uname = Entry(self.frame1, text="User Name", width=20)
        self.entry_uname.pack()
        self.entry_uname.bind("<Return>", self.returnKey_pressed)

        self.entry_pw = Entry(self.frame1, text="Password", width=20, show="*",)
        self.entry_pw.pack()
        self.entry_pw.bind("<Return>", self.returnKey_pressed)

        self.button1 = ttk.Button(self.frame1, text="Login", command=self.validate_login)
        self.button1.pack()

        self.wrongMsg = ttk.Label(self.frame1, text="Username or password is wrong", foreground="red")

    #when return key is pressed after filling out Username field
    #or Password field, it will run validate_login()
    #as if you had pressed the "login" button
    def returnKey_pressed(self, event):
        g = repr(event.char) #gets the representation of the key binding that is bound to the entry fields. aka <Return>
        q = repr("\r")
        if g == q:
            self.validate_login()
        else:
            print("something went wrong")


    def validate_login(self) -> "function":
        self.un = self.entry_uname.get()
        self.pw = self.entry_pw.get()
        if (self.pw == "password") and (self.un == "zach"):
            return open_window() #function from imported text_reader_app
        else:
            return self.error_msg()


    #display error message for 3 seconds, then unpack it making it disappear#
    #will need to create separate thread to run this
    #so the mainloop doesn't 'sleep' and freeze
    #doesn't work with after() either - still freezes
    def error_msg(self):
        self.wrongMsg.pack() #label found in __init__


def main():
    root = Tk()
    root.geometry("300x90")
    root.title("Login")
    app = App(root)
    root.mainloop()

if __name__ == "__main__": main()
