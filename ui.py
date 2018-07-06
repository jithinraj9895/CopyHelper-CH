import webbrowser as wb
from selenium import webdriver
import tkinter as tk
from tkinter import ttk
t = tk.Tk()
t.title('Elves')

loc = ttk.Label(t,text = 'Give Location Below').pack()
def click():
    v = text.get()
    with open(text.get() + '/file.txt', 'r') as open_file:
        line = open_file.readline()
        line = line[:12] + 'ss' + line[12:]
        print(line)
        wb.open(line)


text = tk.StringVar()
e1 = ttk.Entry(t,textvariable = text).pack()


b = tk.Button(t,text = 'lets GO' ,width = 20,command =click)
b.pack()
t.mainloop()



