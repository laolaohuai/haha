
import zipfile
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import threading
import sys
import os
tk = Tk()
tk.title("Zip file extract")

pd_li = []
f = open(os.getcwd()+"\\常用密码.txt")
line = 1
while line:
    line = f.readline()
    pd_li.append(line)
f.close()



def main_func():

    def password_broker():
        filename = tkinter.filedialog.askopenfilename(title="Open a zip file to extract.", filetypes=[("Zip Files", ".zip")])
        for each in pd_li:
            print(each)
            try:
                the_file = zipfile.ZipFile(filename)
                the_file.extractall(pwd=bytes(each, "utf-8"))
                print(each)
                break
            except:
                pass

    thread = threading.Thread(target=password_broker)
    thread.start()


def _quit():
    cmd = tkinter.messagebox.askyesno("Zip File Extract", "Are you sure you want to quit?")
    if cmd:
        tk.destroy()
        sys.exit()


B = Button(tk, text="Extract All", command=main_func)
B.grid(row=0, column=0)
tk.protocol("WM_DELETE_WINDOW", _quit)
tk.mainloop()
