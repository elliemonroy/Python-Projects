
import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        # Created a button 
        self.btn = Button(self.master, text ="Default HTML Page", width =30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1,padx=(10,10) , pady=(10,10))
        # Created a button 
        self.btn = Button(self.master, text ="Submit Custom Text", width =30, height=2, command=self.customText)
        self.btn.grid(row=2, column=2, padx=(10,10) , pady=(10,10))
        # Created a label 
        self.lbl = Label(self.master, text="Enter custom text or click the Default HTML Page button", width =60)
        self.lbl.grid(row=0, column=0, padx=(10,10) , pady=(10,10))
        # Created an entry widget
        self.text = Entry(self.master, text=" ", width =60)
        self.text.grid(row=1, column=0, padx=(10,10) , pady=(10,10))

    # Created function that opens a window on the browser that displays a message
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Created function that takes user input as text and then displays it in a new tab on the browser
    def customText(self):
        string = self.text.get()
        self.text.configure(text=string)
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + string
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        












if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
