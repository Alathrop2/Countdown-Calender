from logging import root
import tkinter as tk
from tkinter import Canvas, filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=400, bg='black')
canvas.pack()

frame = tk.Frame(root, bg='blue')
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

root.mainloop()
