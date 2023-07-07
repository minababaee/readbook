from tkinter.filedialog import askopenfilename
import PyPDF2
from tkinter import *
import pyttsx3

window = Tk()
window.title("read book")

window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

def open_file():
    file= askopenfilename(title="Select a PDF", filetype=(("PDF Files","*.pdf"),("All Files","*.*")))

def read_file():
    pass

txt_edit = Text(window)
frm_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(frm_buttons, text="open", command=open_file)
btn_read = Button(frm_buttons, text="read file", command=read_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_read.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()